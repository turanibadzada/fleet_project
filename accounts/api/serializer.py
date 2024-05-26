from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.serializerfields import PhoneNumberField
from services.generator import CodeGenerator
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes

User = get_user_model()

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    
    class Meta:
        model = User
        fields = ("email", "password")

    def get_user(self):
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        return authenticate(email=email, password=password)

    def create(self, validated_data):
        return self.get_user()
    
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            raise serializers.ValidationError({"error": "No account with this email."})
        
        if not user.check_password(password):
            raise serializers.ValidationError({"error": "Password is wrong."})

        if not user.is_active:
            raise serializers.ValidationError({"error": "This account is not activate."})
    
        return super().validate(attrs)
    
    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return repr_
    


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    name = serializers.CharField(required=True, write_only=True)
    surname = serializers.CharField(required=True, write_only=True)
    mobile = PhoneNumberField()
    password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    password_confirm = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "surname",
            "mobile",
            "password",
            "password_confirm",
        )

    def validate(self, attrs):
        email = attrs.get("email")
        name = attrs.get("name").strip()
        surname = attrs.get("surname").strip()
        mobile = attrs.get("mobile")
        password = attrs.get("password").strip()
        password_confirm = attrs.get("password_confirm").strip()


        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "This email is already exists."})
        if not name.isalpha() or not surname.isalpha():
            raise serializers.ValidationError({"error": "Name and Surname must consist of letters only."})
        if User.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError({"error": "This number is already exists."})
        if password != password_confirm:
            raise serializers.ValidationError({"error": "Passwords did not match."})
        if len(password_confirm) < 8:
            raise serializers.ValidationError({"error": "Password must contain at least 8 character."})
        if not any (_.isdigit() for _ in password):
            raise serializers.ValidationError({"error": "The password must contain at least 1 number and letters."})
        if not any(_.isupper() for _ in password):
            raise serializers.ValidationError({"error": "There must be at least 1 uppercase letter in the password."})
        
        return super().validate(attrs)
    

    def create(self, validated_data):
        password_confirm = validated_data.pop("password_confirm")
        user = User.objects.create(
            **validated_data,
            is_active = False,
            activation_code = CodeGenerator().create_user_activation_code(size=6, model_=User)
        )
        # Activation mail
        send_mail(
            "Activate Your Travel Page Account",
            f"Your activation code: {user.activation_code}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=True
        )
        user.set_password(password_confirm)
        user.save()
        return user
    

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        uuid = urlsafe_base64_encode(smart_bytes(instance.id))
        repr_["uuid"] = uuid
        return repr_



class ActivationSerializer(serializers.ModelSerializer):
    activation_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("activation_code", )

    
    def validate(self, attrs):
        activation_code = attrs.get("activation_code")
        user = self.instance
        if not user.activation_code == activation_code:
            raise serializers.ValidationError({"error": "Code is wrong."})
        return super().validate(attrs)
    

    def update(self, instance, validated_data):
        instance.is_active = True
        instance.activation_code = None
        instance.save()
        return instance
    

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return repr_



class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    uuid = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ("uuid", "email")


    def validate(self, attrs):
        email = attrs.get("email")
        try:
            user = User.objects.get(email=email)
        except:
            raise serializers.ValidationError({"error": "There is no user with this e-mail address."})
        
        if not user.is_active:
            raise serializers.ValidationError({"error": "This account is not active."})
        return super().validate(attrs)
    
    def get_uuid(self, obj):
        return urlsafe_base64_encode(smart_bytes(obj.id))
    
    def create(self, validated_data):
        user = User.objects.get(email=validated_data.get("email"))
        user.activation_code = CodeGenerator().create_user_activation_code(size=6, model_=User)
        user.save()

        #send code to email
        send_mail(
            "Activate Your Travel Page Account",
            f"Your reset code: {user.activation_code}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=True
        )
        return user
        


class ResetPasswordCheckSerializers(serializers.ModelSerializer):
    uuid = serializers.SerializerMethodField(read_only=True)
    activation_code = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("uuid", "activation_code")
        

    def validate(self, attrs):
        user = self.instance
        activation_code = attrs.get("activation_code")


        if not user.activation_code == activation_code:
            raise serializers.ValidationError({"error": "Code is wrong."})
        return super().validate(attrs)
    

    def get_uuid(self, obj):
        return urlsafe_base64_encode(smart_bytes(obj.id))
    

    def update(self, instance, validated_data):
        instance.activation_code = None
        instance.save()
        return instance
    


class ResetPasswordCompleteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    password_confirm = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})


    class Meta:
        model = User
        fields = ("email", "password", "password_confirm")

        extra_kwargs = {"email": {"read_only": "True"}}


    def validate(self, attrs):
        user = self.instance
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")


        if len(password) < 8:
            raise serializers.ValidationError({"error": "Password must contain at least 8 character."})
        if user.check_password(password):
            raise serializers.ValidationError({"error": "You have used this password."})
        if not password == password_confirm:
            raise serializers.ValidationError({"error": "Passwords did not match."})
        if not any (_.isdigit() for _ in password):
            raise serializers.ValidationError({"error": "The password must contain at least 1 number and leters."})
        if not any (_.isupper() for _ in password_confirm):
            raise serializers.ValidationError({"error": "The password must contain at least 1 uppercase letter."})
        return super().validate(attrs)
    

    def update(self, instance, validated_data):
        password = validated_data.get("password")
        instance.set_password(password)
        instance.save()
        return instance
    

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return repr_
    


class ChangePasswordSeralizers(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    new_password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    new_password_confirm = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ("old_password", "new_password", "new_password_confirm")


    def validate(self, attrs):
        user = self.instance
        old_password = attrs.get("old_password")
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.get("new_password_confirm")


        if not user.check_password(old_password):
            raise serializers.ValidationError({"error": "Old password is wrong."})
        if len(new_password) < 8:
            raise serializers.ValidationError({"error": "The new password must contain at least 8 character."})
        if user.check_password(new_password):
            raise serializers.ValidationError({"error": "You have used this password."})
        if not new_password == new_password_confirm:
            raise serializers.ValidationError({"error": "Passwords did not match."})
        if not any (_.isdigit() for _ in new_password):
            raise serializers.ValidationError({"error": "The password must contain at least 1 number and letters."})
        if not any (_.isupper() for _ in new_password_confirm):
            raise serializers.ValidationError({"error": "The password must contain at least 1 uppercase letter."})
        
        return super().validate(attrs)
        

    def update(self, instance, validated_data):
        new_password = validated_data.get("new_password")
        instance.set_password(new_password)
        instance.save()
        return instance
    

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return repr_
    


class ProfileEditSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "name",
            "surname",
            "bio",
            "profile_photo",
            "mobile",
            "location",
            "social",
        )
        extra_kwargs = {
            "location": {"write_only": True}
        }
    def get_location(self, obj):
        return obj.location.name


class ProfileDeleteSerializer(serializers.ModelSerializer):
    uuid = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = User
        fields = ("uuid", "email")

        extra_kwargs = {
            "email": {"write_only": True}
        }


    def get_uuid(self, obj):
        uuid = urlsafe_base64_encode(smart_bytes(obj.id))
        return uuid
    

    def create(self, validated_data):
        user = self.context.get("user")
        user.activation_code = CodeGenerator().create_user_activation_code(size=6, model_=User)
        user.save()
        send_mail(
            "Travel Page",
            f"Delete Account\n Your account delete code: {user.activation_code}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=True
        )
        return user
    


class ProfilelDeleteCheckSerializer(serializers.ModelSerializer):
    uuid = serializers.SerializerMethodField(read_only=True)
    activation_code = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("uuid", "activation_code")


    def validate(self, attrs):
        user = self.instance
        activation_code = attrs.get("activation_code")

        if not user.activation_code == activation_code:
            raise serializers.ValidationError({"error": "Wrong code."})
        return super().validate(attrs)
    

    def get_uuid(self, obj):
        return urlsafe_base64_encode(smart_bytes(obj.id))
    

    def update(self, instance, validated_data):
        instance.delete()
        return instance



class UserSeriazlier(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "logo",
            "email",
        )
                  







        
        
                                    






    
    

        
        

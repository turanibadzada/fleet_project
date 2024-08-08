from rest_framework import serializers
from ..models import Vacancies, JobApplication, Projects
import pathlib
from accounts.api.serializer import UserSeriazlier



class VacanciesListSeriazlizer(serializers.ModelSerializer):

    class Meta:
        model = Vacancies
        fields = (
            "name", 
            "image", 
            "view_count",
        )



class VacanciesDetailSeriazlier(serializers.ModelSerializer):

    class Meta:
        model = Vacancies
        fields = (
            "name",
            "salary",
            "type",
            "job_summary",
            "image",
            "status",
            "responsibilities",
            "requirements",
            "working_condition",
            "view_count",
        )



class JobApplicationListSerializer(serializers.ModelSerializer):
    vacancy_name = serializers.SerializerMethodField()
   
    class Meta:
        model = JobApplication
        fields = ("id","vacancy_name", "fullname")

    def get_vacancy_name(self, obj):
        return obj.vacancy.name

        
        
        
class JobApplicationDetailSerializer(serializers.ModelSerializer):
    vacancy_name = serializers.SerializerMethodField()

    class Meta:
        model = JobApplication
        fields = (
            "vacancy_name",
            "fullname",
            "email",
            "mobile",
            "self_information",
            "cv",
        )

    def get_vacancy_name(self, obj):
        return obj.vacancy.name
    
   

class JobApplicationCreateSerializer(serializers.ModelSerializer):
    vacancy_name = serializers.SerializerMethodField()

    class Meta:
        model = JobApplication
        fields = (
            "vacancy",
            "fullname",
            "email",
            "mobile",
            "self_information",
            "cv",
            "vacancy_name"
        )
        extra_kwargs = {
            "vacancy": {"write_only":True}
        }

    def get_vacancy_name(self, obj):
        return obj.vacancy.name
    

    def validate(self, attrs):
        file = attrs.get("cv")
        if file:
            if file is not None and file is not False:
                file_path = pathlib.Path(str(file)).suffix
                if file_path not in ['.pdf', '.pdfa', '.pdfx','.pdfvt','.pdfua']:
                    raise serializers.ValidationError( "CV can be uploaded only in .pdf, .pdfa, .pdfx, .pdfvt and .pdfua format.")
        return super().validate(attrs)



class ProjectsListSerializer(serializers.ModelSerializer):
    user = UserSeriazlier()

    class Meta:
        model = Projects
        fields = (
            "id",
            "user",
            "position",
        )    
  

    def get_user(self, obj):
        return f"{obj.user.name} {obj.user.surname}"
    


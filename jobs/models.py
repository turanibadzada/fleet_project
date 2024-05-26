from django.db import models
from ckeditor.fields import RichTextField
from services.mixin import DateMixin, BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from services.choices import WORK_TYPE, STATUS, WORKING_CONDITION, POSITION_CHOICES
from django.contrib.auth import get_user_model


User = get_user_model()



class Vacancies(BaseModel, DateMixin):
    salary = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=WORK_TYPE, blank=True, null=True)
    job_summary = models.TextField()
    image = models.ImageField(upload_to="vacancies/", blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default="Active")
    responsibilities = RichTextField()
    requirements = RichTextField()
    working_condition = models.CharField(max_length=50, choices=WORKING_CONDITION)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"



class JobApplication(DateMixin):
    vacancy = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = PhoneNumberField()
    self_information = models.TextField()
    cv = models.FileField(upload_to="vacancies/", blank=True, null=True)

    def __str__(self):
        return self.vacancy.name
    
    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Job Application"



class Projects(DateMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=300, choices=POSITION_CHOICES)

    def __str__(self):
        return self.position
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"




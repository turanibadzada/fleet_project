from rest_framework import generics
from ..models import Vacancies, JobApplication, Projects
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    VacanciesListSeriazlizer, VacanciesDetailSeriazlier, JobApplicationListSerializer, 
    JobApplicationDetailSerializer, JobApplicationCreateSerializer, ProjectsListSerializer)



class VacanciesListView(generics.ListAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesListSeriazlizer



class VacanciesDetailView(generics.RetrieveAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesDetailSeriazlier
    lookup_field = "id"



class JobApplicationListView(generics.ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return JobApplication.objects.filter(email=self.request.user.email)
    


class JobApplicationDetailView(generics.RetrieveAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationDetailSerializer
    lookup_field = "id"



class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationCreateSerializer



class ProjectsListView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsListSerializer

from .import views
from django.urls import path

app_name = "jobs_api"


urlpatterns = [
    path("vacancies/", views.VacanciesListView.as_view(), name="vacancies"),
    path("vacancies/detail/<id>/", views.VacanciesDetailView.as_view(), name="vacancies-detail"),
    path("application/", views.JobApplicationListView.as_view(), name="job-application"),
    path("application/detail/<id>/", views.JobApplicationDetailView.as_view(), name="job-application-detail"),
    path("application/create/", views.JobApplicationCreateView.as_view(), name="job-application-create"),
    path("projects/", views.ProjectsListView.as_view(), name="projects"),
]
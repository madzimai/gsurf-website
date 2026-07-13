from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("research/", views.research, name="research"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.news, name="news"),
    path("team/<int:id>/", views.team_detail, name="team_detail"),
    path("projects/",views.projects,name="projects"),
    path("projects/<slug:slug>/",views.project_detail,name="project_detail"),
]
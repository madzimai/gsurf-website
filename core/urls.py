from django.urls import path
from django.contrib.auth import views as auth_views
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
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login",),
    path("news/<int:id>/", views.news_detail, name="news_detail"),

path(
    "logout/",
    auth_views.LogoutView.as_view(next_page="home"),
    name="logout",
),
]
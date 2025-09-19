from django.urls import path
from app import views  # Import views from the app

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("tech", views.tech, name="tech"),
    path("sol", views.sol, name="sol"),
    path("innov", views.innov, name="innov"),
    path("impact", views.impact, name="impact"),

]

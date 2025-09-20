from django.urls import path
from app import views  # Import views from the app

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("about.html", views.about, name="about_html"),  # Handle .html extension
    path("tech", views.tech, name="tech"),
    path("tech.html", views.tech, name="tech_html"),  # Handle .html extension
    path("sol", views.sol, name="sol"),
    path("sol.html", views.sol, name="sol_html"),  # Handle .html extension
    path("innov", views.innov, name="innov"),
    path("innov.html", views.innov, name="innov_html"),  # Handle .html extension
    path("impact", views.impact, name="impact"),
    path("impact.html", views.impact, name="impact_html"),  # Handle .html extension
]

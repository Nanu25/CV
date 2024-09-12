from django.urls import path

from cvsite import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("contact", views.contact, name="contact"),
]
from django.urls import path

from cvsite import views

urlpatterns = [
    path("", views.index, name="index"),
]
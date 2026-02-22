from django.urls import path

from cvsite import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("journal/<int:entry_id>/", views.journal_entry, name="journal_entry"),
]
from django.urls import path

from . import views

urlpatterns = [
    path("songs/<int:pk>", views.SongView.as_view()),
]

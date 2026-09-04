from django.urls import path
from . import views

urlpatterns = [
    path("allvideos/", views.video_view, name="allvideos"),
    path("create_video/", views.create_video_view, name="create_video"),
]
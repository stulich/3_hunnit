from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path("discussionPosts/", views.discussionPosts, name="discussionPosts"),
]


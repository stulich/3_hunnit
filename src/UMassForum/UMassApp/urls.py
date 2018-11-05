from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name='index'),
    path("surveyposts/", views.surveyPosts, name="surveyPosts"),
    path("createsurvey/", views.createsurvey, name="createsurvey"),
    path('surveyresults/', views.surveyResults, name="surveyresults"),
    path("discussionposts/", views.discussionPosts, name="discussionPosts"),
    path("discussioncreation/", views.createDiscussion, name="discussioncreation"),

]
      
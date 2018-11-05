from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name='index'),
    path("surveyposts/", views.surveyPosts, name="surveyPosts"),
    path("createsurvey/", views.createsurvey, name="createsurvey"),
    # path('surveyresults/', views.surveyResults, name="surveyresults"),
    path("discussionposts/", views.discussionPosts, name="discussionPosts"),
    path("surveyresults/", views.surveyResults.as_view(),name="survey_results"),

 
]
      
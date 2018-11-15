from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name='index'),
    path("surveyposts/", views.surveyPosts, name="surveyPosts"),
    path("createsurvey/", views.createsurvey, name="createsurvey"),
    # path('surveyresults/', views.surveyResults, name="surveyresults"),
    path("discussionposts/", views.discussionPosts.as_view(), name="discussion_posts"),
    path("surveyresults/", views.surveyResults.as_view(),name="survey_results"),
    path("discussioncreation/", views.createDiscussion, name="discussioncreation"),
    path(r'^surveyresults/(?P<pk>[0-9A-Fa-f-]+)', views.SurveyPostsView.as_view(), name="survey-post-detail"),
    path(r'^discussionposts/(?P<pk>[0-9A-Fa-f-]+)', views.discussionDetails.as_view(), name="discussion-post-detail"),
    path( "user/", views.UserGeneralView.as_view(), name="userindividual" ),
]
      
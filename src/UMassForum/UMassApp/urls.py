from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name='index'),
    path("surveyposts/", views.SurveyPostsView.as_view(), name="surveyposts"),
    path("createsurvey/", views.createsurvey, name="createsurvey"),
    path('surveyresults/', views.surveyResults, name="surveyresults"),
    # path('surveyresults/<int:surveypost_id>/', views.surveyResults, name="surveyresults"),
#     path('<int:pk>/', views.SPDetailsView.as_view(), name='spdetails'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:surveypost_id>/vote/', views.vote, name='vote'),
#  
]
      
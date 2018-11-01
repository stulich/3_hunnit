from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("discussionPosts/", views.discussionPosts, name="discussionPosts"),
    path('<int:pk>/', views.SPDetailsView.as_view(), name='spdetails'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:surveypost_id>/vote/', views.vote, name='vote'),
]


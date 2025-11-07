from rest_framework.urls import path
from .views import ResumeJobMatchView
urlpatterns = [
    path('match/<int:id>/',ResumeJobMatchView.as_view(),name = 'resume-job-match'), 
]

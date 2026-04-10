from django.urls import path
from .views import *


urlpatterns = [
    path('candidates/', CandidateListCreateView.as_view()),
    path('applications/', ApplicationListCreateView.as_view()),
    path('applications/<int:pk>/notes/', InterviewNoteListCreateView.as_view()),
    path('summary/', SummaryView.as_view()),
]
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Count
from .models import Candidate, Application, InterviewNote
from .serializers import CandidateSerializer, ApplicationSerializer,InterviewNoteSerializer

# Create your views here.

class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class ApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    
    def get_queryset(self):
        queryset = Application.objects.all()
        status = self.request.query_param.get('status')
        
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class InterviewNoteListCreateView(generics.ListCreateAPIView):
    serializer_class = InterviewNoteSerializer
    
    def get_queryset(self):
        return InterviewNote.objects.filter(application_id=self.kwargs['pk'])
    
    def perform_create(self, serializer):
        serializer.save(application_id=self.kwargs['pk'])


class SummaryView(generics.GenericAPIView):
    def get(self, request):
        data = Application.objects.values('status').annotate(count=Count('id'))
        return Response(data)
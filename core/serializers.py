from rest_framework import serializers
from .models import Candidate, Application, InterviewNote


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
    
    
    def validate_email(self, value):
        if Candidate.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        

class InterviewNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewNote
        fields = '__all__'
    
    
    def Validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Rating must not be less than 1')
        return value
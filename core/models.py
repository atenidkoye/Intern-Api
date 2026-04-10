from django.db import models

# Create your models here.

class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    years_of_experience = models.IntegerField()
    primary_skill = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('screening', 'Screening'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]
  
    
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    position = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    source = models.CharField(max_length=100)
    applied_at = models.DateTimeField(auto_now_add=True)


class InterviewNote(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
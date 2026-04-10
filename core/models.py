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
        ('applied', 'Applied')
        ('screening', 'Screening')
        ('interview', 'Interview')
        ('rejected', 'Rejected')
        ('accepted', 'Accepted')
    ]
    
    
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Candidate, Application

# Create your tests here.

class APITests(APITestCase):
    
    def test_create_candidate(self):
        res = self.client.post('/api/candidates/', {
            'full_name': 'Abraham Morrrison',
            'email': 'abraham@gmail.com',
            'phone': '123456789',
            'years_of_experience': 2,
            'primary_skill': 'python'
        })
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        

    
    def test_duplicate_email(self):
        Candidate.objects.create(
            full_name = 'Abraham',
            email = 'abrham@gamil.com',
            phone= '123456789',
            years_of_experience = 2,
            primary_skill = 'python'
        )
        
        res = self.client.post('/api/candidates/', {
            'full_name': 'abraham',
            'email': 'abaham@gmail.com',
            'phone': '358',
            'years_of_experience': 3,
            'primary_skill': 'django'
            
        })
        self.assertEqual(res.status_code, 400)
    
    
    def test_create_application(self):
        candidate = Candidate.objects.create(
            full_name = 'abraham',
            email = 'abraha@yahoo.com',
            phone = '456',
            years_of_experience = 4,
            primary_skill = 'java'
        )
        res=self.client.post('/api/applications/', {
            'candidate': candidate.id,
            'position': 'backend intern',
            'status': 'applied',
            'source': 'instagram'
        })
        self.assertEqual(res.status_code, 201)
    
    def test_filter_by_status(self):
        res = self.client.get('/api/applications/?status=interview')
        self.assertEqual(res.status_code, 200)
    
    def test_summary(self):
        res = self.client.get('/api/summary/')
        self.assertEqual(res.status_code, 200)
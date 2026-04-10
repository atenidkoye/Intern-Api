from django.contrib import admin
from django.contrib import admin
from .models import Candidate, Application, InterviewNote


# Register your models here.

admin.site.register(Candidate)
admin.site.register(Application)
admin.site.register(InterviewNote)
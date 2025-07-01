from django.shortcuts import render
from project.models import Project

def homepage(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'projects': projects})

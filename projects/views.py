from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.
def all_projects(request):
    # query te db to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                    {'projects': projects})

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/details.html',
    {'projects': projects})
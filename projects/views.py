from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from projects.models import Project
import pytz


# Create your views here.

def all_projects(request):
    # query te db to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                    {'projects': projects})

def project_details(request, pk):
    projects = Project.objects.get(pk=pk)
    return render(request, 'projects/details.html',
    {'projects': projects})


# def all_projects(request):
#     user_timezone = request.GET.get('user_timezone', None)

#     if user_timezone is not None:
#         try:
#             user_tz = pytz.timezone(user_timezone)
#         except pytz.UnknownTimeZoneError:
#             user_tz = timezone.utc
#     else:
#         user_tz = timezone.utc

#     projects = Project.objects.all()

#     context = {
#         'projects': projects,
#         'user_timezone': user_tz,  # Pass the user's timezone to the template
#     }

#     return render(request, 'projects/all_projects.html', context)


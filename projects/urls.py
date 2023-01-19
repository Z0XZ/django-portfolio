from django.urls import include, path
from projects import views

urlpatterns = [
    path('', views.all_projects),
    path('<int:pk>', views.project_detail),
]
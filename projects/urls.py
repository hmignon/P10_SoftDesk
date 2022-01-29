from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('', views.project_list),
    path('<int:project_pk>/', views.project_detail),
    path('<int:project_pk>/users/', views.contributor_list),
    path('<int:project_pk>/users/<int:contributor_pk>/', views.contributor_detail),
    path('<int:project_pk>/issues/', views.issue_list),
    path('<int:project_pk>/issues/<int:issue_pk>/', views.issue_detail),
    path('<int:project_pk>/issues/<int:issue_pk>/comments/', views.comment_list),
    path('<int:project_pk>/issues/<int:issue_pk>/comments/<int:comment_pk>/', views.comment_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

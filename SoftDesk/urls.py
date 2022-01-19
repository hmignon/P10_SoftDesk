from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from projects import views


# TODO add login and signup
urlpatterns = [
    # path('signup/'),
    # path('login/'),
    path('projects/', views.project_list),
    path('projects/<int:project_pk>/', views.project_detail),
    path('projects/<int:project_pk>/users/', views.contributor_list),
    path('projects/<int:project_pk>/users/<int:contributor_pk>/', views.contributor_detail),
    path('projects/<int:project_pk>/issues/', views.issue_list),
    path('projects/<int:project_pk>/issues/<int:issue_pk>', views.issue_detail),
    path('projects/<int:project_pk>/issues/<int:issue_pk>/comments/', views.comment_list),
    path('projects/<int:project_pk>/issues/<int:issue_pk>/comments/<int:comment_pk>/', views.comment_detail),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

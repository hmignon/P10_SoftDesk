from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('projects/', include('projects.urls')),
]

from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from projects import views


# Routers provide an easy way of automatically determining the URL conf.
"""
router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet, basename='projects')
router.register(r"^(?P<id>[^/.]+)/users", views.ContributorViewSet, basename="users")
router.register(r"^(?P<id>[^/.]+)/issues", views.IssueViewSet, basename="issues")
router.register(r"^(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", views.CommentViewSet, basename="comments")
"""

# TODO add login and signup
urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from projects import views


"""
router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet, basename='projects')
router.register(r"^(?P<id>[^/.]+)/users", views.ContributorViewSet, basename="users")
router.register(r"^(?P<id>[^/.]+)/issues", views.IssueViewSet, basename="issues")
router.register(r"^(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", views.CommentViewSet, basename="comments")
"""

# TODO add login and signup
urlpatterns = [
    # path('signup/'),
    # path('login/'),
    path('projects/', views.project_list),
    path('projects/<int:pk>/', views.project_detail),
    path('projects/<int:pk>/users/', views.contributor_list),
    path('projects/<int:pk1>/users/<int:pk2>/', views.contributor_detail),
    path('projects/<int:pk>/issues/', views.issue_list),
    path('projects/<int:pk1>/issues/<int:pk2>', views.issue_detail),
    path('projects/<int:pk1>/issues/<int:pk2>/comments/', views.comment_list),
    path('projects/<int:pk1>/issues/<int:pk2>/comments/<int:pk3>/', views.comment_detail),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path, include
from rest_framework_nested import routers

from projects import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet)

p_router = routers.NestedDefaultRouter(router, 'projects', lookup='project')
p_router.register('issues', views.IssueViewSet)
p_router.register('contributors', views.ContributorViewSet)

i_router = routers.NestedDefaultRouter(p_router, 'issues', lookup='issue')
i_router.register('comments', views.CommentViewSet)


# TODO add login and signup
urlpatterns = [
    path('', include(router.urls)),
    path('', include(p_router.urls)),
    path('', include(i_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

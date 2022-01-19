from rest_framework import permissions

from .models import Project


class ProjectPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author
        else:
            return False


class Permissions(permissions.BasePermission):
    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        user_projects = Project.objects.filter(contributors__user=request.user)
        if project in user_projects:
            project = Project.objects.get(id=view.kwargs['project_pk'])
            if request.method == 'GET':
                return request.user
            elif request.method in ['PUT', 'DELETE']:
                return request.user == project.author
            else:
                return False

    def has_object_permission(self, request, view, obj):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if request.method == 'GET':
            return request.user
        elif request.method in ['PUT', 'DELETE']:
            return request.user == project.author
        else:
            return False

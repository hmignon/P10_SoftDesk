from rest_framework import permissions

from .models import Project


class ProjectPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author


class ContributorPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        user_projects = Project.objects.filter(contributors__user=request.user)
        if project in user_projects:
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user == project.author
        return False

    def has_object_permission(self, request, view, obj):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == project.author


class IssueCommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        user_projects = Project.objects.filter(contributors__user=request.user)
        if project in user_projects:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author

from rest_framework import permissions

from .models import Project, Issue, Comment


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

    def has_object_permission(self, request, view, obj):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == project.author


class IssuePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        user_projects = Project.objects.filter(contributors__user=request.user)
        issue = Issue.objects.get(id=view.kwargs['issue_pk'])
        if project in user_projects:
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user == issue.author

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author


class CommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        user_projects = Project.objects.filter(contributors__user=request.user)
        comment = Comment.objects.get(id=view.kwargs['comment_pk'])
        if project in user_projects:
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user == comment.author

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project, Issue, Contributor, Comment
from .permissions import ProjectPermissions, IssuePermission, CommentPermission
from .serializers import (
    UserSerializer,
    ProjectSerializer,
    IssueSerializer,
    CommentSerializer,
    ContributorsSerializer,
)


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


"""

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        return User.objects.filter(project_id=project)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, ProjectPermissions]

    def get_queryset(self):
        return Project.objects.filter(contributors__user=self.request.user)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['author'] = request.user.id
        serialized_data = ProjectSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        project = serialized_data.save()
        contributor = Contributor.objects.create(
            user=request.user,
            project=project,
            role='author',
        )
        contributor.save()


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        return Contributor.objects.filter(project_id=project)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IssuePermission]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        return Issue.objects.filter(project_id=project)

    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        serializer.save(project_id=project)
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermission]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])

    def perform_create(self, serializer):
        query_issue_id = self.kwargs.get('issue')
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        issues = Issue.objects.filter(project_id=project)
        issue = issues.get(pk=query_issue_id)
        serializer.save(issue=issue)
        serializer.save(author=self.request.user)
        
"""

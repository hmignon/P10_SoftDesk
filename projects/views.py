from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Project, Issue, Contributor, Comment
from .permissions import (
    ProjectPermissions,
    ContributorPermissions,
    IssuePermissions,
    CommentPermissions,
)
from .serializers import (
    ProjectSerializer,
    IssueSerializer,
    CommentSerializer,
    ContributorSerializer,
)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ProjectPermissions])
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.filter(contributors__user=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data.copy()
        data['author'] = request.user.id

        serializer = ProjectSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            project = serializer.save()
            Contributor.objects.create(user=request.user, project=project, role='AUTHOR')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ProjectPermissions])
def project_detail(request, project_pk):
    project = get_object_or_404(Project, id=project_pk)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data.copy()
        data['author'] = project.author.id

        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response('Project successfully deleted.', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ContributorPermissions])
def contributor_list(request, project_pk):
    project = get_object_or_404(Project, id=project_pk)

    if request.method == 'GET':
        contributors = Contributor.objects.filter(project=project)
        serializer = ContributorSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data.copy()
        data['project'] = project.id

        try:
            Contributor.objects.get(user=data['user'], project=project.id)
            return Response('This user has already been added.', status=status.HTTP_400_BAD_REQUEST)
        except Contributor.DoesNotExist:
            try:
                User.objects.get(id=data['user'])
                serializer = ContributorSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                return Response('This user does not exist.', status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ContributorPermissions])
def contributor_detail(request, project_pk, contributor_pk):
    get_object_or_404(Project, id=project_pk)
    contributor = get_object_or_404(Contributor, id=contributor_pk)

    if request.method == 'DELETE':
        if contributor.role == 'AUTHOR':
            return Response('Project author cannot be deleted.', status=status.HTTP_400_BAD_REQUEST)
        else:
            contributor.delete()
            return Response('Contributor successfully deleted.', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IssuePermissions])
def issue_list(request, project_pk):
    project = get_object_or_404(Project, id=project_pk)

    if request.method == 'GET':
        issues = Issue.objects.filter(project=project)
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data.copy()
        data['project'] = project.id
        data['author'] = request.user.id

        try:
            Contributor.objects.get(id=data['assignee'], project=project.id)
            serializer = IssueSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Contributor.DoesNotExist:
            return Response(
                'This user is not contributing to this project or does not exist.',
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IssuePermissions])
def issue_detail(request, project_pk, issue_pk):
    project = get_object_or_404(Project, id=project_pk)
    issue = get_object_or_404(Issue, id=issue_pk)

    if request.method == 'PUT':
        data = request.data.copy()
        data['project'] = project.id
        data['author'] = issue.author.id

        try:
            Contributor.objects.get(id=data['assignee'], project=project.id)
            serializer = IssueSerializer(issue, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Contributor.DoesNotExist:
            return Response(
                'This user is not contributing to this project or does not exist.',
                status=status.HTTP_400_BAD_REQUEST
            )

    elif request.method == 'DELETE':
        issue.delete()
        return Response('Issue successfully deleted.', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, CommentPermissions])
def comment_list(request, project_pk, issue_pk):
    get_object_or_404(Project, id=project_pk)
    issue = get_object_or_404(Issue, id=issue_pk)

    if request.method == 'GET':
        comments = Comment.objects.filter(issue=issue)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data.copy()
        data['issue'] = issue.id
        data['author'] = request.user.id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, CommentPermissions])
def comment_detail(request, project_pk, issue_pk, comment_pk):
    get_object_or_404(Project, id=project_pk)
    issue = get_object_or_404(Issue, id=issue_pk)
    comment = get_object_or_404(Comment, id=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data.copy()
        data['issue'] = issue.id
        data['author'] = comment.author.id

        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response('Comment successfully deleted.', status=status.HTTP_204_NO_CONTENT)

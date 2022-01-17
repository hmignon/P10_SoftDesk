from django.contrib.auth.models import User
from rest_framework import serializers

from projects.models import Project, Contributor, Issue, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author']


class ContributorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = "__all__"


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

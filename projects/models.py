from django.conf import settings
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.CharField(
        choices=[
            ('Backend', 'Backend'),
            ('Frontend', 'Frontend'),
            ('iOS', 'iOS'),
            ('Android', 'Android')
        ],
        max_length=128
    )
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    permission = models.CharField(max_length=150, choices='')
    role = models.CharField(max_length=150)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.TextField(max_length=2048)
    tag = models.CharField(
        choices=[
            ('Bug', 'Bug'),
            ('Task', 'Task'),
            ('Upgrade', 'Upgrade')
        ],
        max_length=20
    )
    priority = models.CharField(
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High')
        ],
        max_length=20
    )
    status = models.CharField(
        choices=[
            ('Todo', 'Todo'),
            ('In progress', 'In progress'),
            ('Done', 'Done')
        ],
        max_length=20
    )
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=2048)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

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
        max_length=8
    )
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributors')
    role = models.CharField(
        max_length=11,
        choices=[
            ('author', 'author'),
            ('contributor', 'contributor')
        ],
        default='contributor'
    )


class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.TextField(max_length=2048)
    tag = models.CharField(
        choices=[
            ('Bug', 'Bug'),
            ('Task', 'Task'),
            ('Upgrade', 'Upgrade')
        ],
        max_length=7
    )
    priority = models.CharField(
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High')
        ],
        max_length=6,
        default='Low'
    )
    status = models.CharField(
        choices=[
            ('Todo', 'Todo'),
            ('In progress', 'In progress'),
            ('Done', 'Done')
        ],
        max_length=11
    )
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee = models.ForeignKey(to=Contributor, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.utils import timezone

from users.models import User


class Project(models.Model):
    title = models.CharField()
    description = models.CharField()
    type = models.CharField()
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Issue(models.Model):
    title = models.CharField()
    desc = models.CharField()
    tag = models.CharField()
    priority = models.CharField()
    status = models.CharField()
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    description = models.CharField()
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

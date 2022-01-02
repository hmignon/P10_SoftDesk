from django.db import models


class User(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    password = models.CharField()


class Contributor(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project_id = models.IntegerField()
    permission = models.Choices()
    role = models.CharField()

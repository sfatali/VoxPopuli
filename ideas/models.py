from django.db import models
from util.models import City
from problems.models import Problem
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField


class Idea(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, blank=True, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=40)
    body = models.TextField()
    image = models.ImageField(blank=True)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="active")
    tags = ArrayField(models.CharField(max_length=30), blank=True, default='')

    class Meta:
        db_table = "ideas"


class IdeaComment(models.Model):
    id = models.UUIDField(primary_key=True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "ideas_comments"

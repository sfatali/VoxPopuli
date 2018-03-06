from django.db import models
from util.models import City
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField


class Problem(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=40, null=False)
    body = models.TextField(null=False)
    image = models.ImageField(blank=True)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="unresolved")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=30), blank=True)

    class Meta:
        db_table = "problems"


class ProblemComment(models.Model):
    id = models.UUIDField(primary_key=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, null=False)
    created_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "problems_comments"

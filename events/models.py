from django.db import models
from util.models import City
from ideas.models import Idea
from django.contrib.auth.models import User
from django.utils.timezone import now


class Event(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField
    event_date = models.DateTimeField()
    created_date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=40)
    body = models.TextField()
    status = models.CharField(max_length=10, default="active")

    class Meta:
        db_table = "events"


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "events_attendance"


class EventComment(models.Model):
    id = models.UUIDField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "events_comments"

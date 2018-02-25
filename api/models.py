from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, null=False, unique=True)
    password = models.CharField(max_length=256, null=False)
    name = models.CharField(max_length=25, null=False)
    surname = models.CharField(max_length=35, null=False)
    birth_date = models.DateField(null=False)
    email = models.EmailField(null=False)
    registered_date = models.DateTimeField(default=now)
    karma = models.IntegerField(default=0)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Problem(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=40, null=False)
    body = models.TextField(null=False)
    image = models.ImageField(blank=True)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="unresolved")
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=30), blank=True)


class Idea(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    problem = models.ForeignKey('Problem', blank=True, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=40, null=False)
    body = models.TextField(null=False)
    image = models.ImageField(blank=True)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="active")
    tags = ArrayField(models.CharField(max_length=30), blank=True, default='')


class Event(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    idea = models.ForeignKey('Idea', on_delete=models.CASCADE)
    event_date = models.DateTimeField(null=False)
    created_date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=40, null=False)
    body = models.TextField(null=False)
    status = models.CharField(max_length=10, default="active")


class UserEvent(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True)
    post_id = models.UUIDField
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, null=False)
    created_date = models.DateTimeField(default=now)


class ReportHistory(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.UUIDField() # id of problem, idea, event. comments can be reported too
    user = models.ForeignKey('User', on_delete=models.CASCADE) # who reported
    reason = models.CharField(max_length=50, null=False) # here will be a set of options added later todo!
    created_date = models.DateTimeField(default=now)


class UserSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.UUIDField
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)


class Continent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    # planet :D


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

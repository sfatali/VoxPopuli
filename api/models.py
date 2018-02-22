from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, null=False, unique=True)
    password = models.CharField(max_length=256, null=False)
    name = models.CharField(max_length=25, null=False)
    surname = models.CharField(max_length=35, null=False)
    registered_date = models.DateTimeField(default=now)
    karma = models.IntegerField(default=0)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)


class Problem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=40, null=False)
    body = models.TextField(null=False)
    image = models.IntegerField
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="unresolved")
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=30), blank=True)


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
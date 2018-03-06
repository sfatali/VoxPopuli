from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Continent(models.Model):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = "continents"


class Country(models.Model):
    name = models.CharField(max_length=50, null=False)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    class Meta:
        db_table = "countries"


class City(models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = "cities"


class ReportHistory(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.UUIDField() # id of event. comments can be reported too
    user = models.ForeignKey(User, on_delete=models.CASCADE) # who reported
    reason = models.CharField(max_length=50) # here will be a set of options added later todo!
    created_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "report_history"

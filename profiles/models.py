from django.db import models
from django.contrib.auth.models import User
from util.models import City


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    about = models.TextField(null=True)
    karma = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = "profiles"

# Generated by Django 2.0.2 on 2018-03-04 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='idea',
            table='ideas',
        ),
        migrations.AlterModelTable(
            name='ideacomment',
            table='ideas_comments',
        ),
    ]
from django.db import models


class Lectures(models.Model):
    id = models.AutoField(primary_key=True)
    lecture_name = models.CharField(max_length=200)


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(null=True)



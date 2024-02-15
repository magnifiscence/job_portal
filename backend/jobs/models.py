from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Qualification(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)


class Company(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)


class Location(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)


class Job(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    salaray = models.IntegerField(default=100000)
    description = models.TextField()
    experiance = models.IntegerField(default=1)
    datestamp = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    category = models.ManyToManyField(Category)
    qualification = models.ManyToManyField(Qualification)
    applicants = models.ManyToManyField(
        User, blank=True, related_name="user_to_job")
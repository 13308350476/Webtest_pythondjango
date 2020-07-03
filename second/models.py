from django.db import models

# Create your models here.


class User(models.Model):
    u_Name = models.CharField(max_length=30, unique=True)
    u_Password = models.CharField(max_length=30)


class Movie(models.Model):
    m_name = models.CharField(max_length=100, null=False)
    m_tag = models.CharField(max_length=30, null=False)


class Grade(models.Model):
    m_name = models.CharField(max_length=100, null=False)
    m_grade = models.CharField(max_length=10, null=True)


class User_tag(models.Model):
    Name = models.CharField(max_length=10, null=False)
    tag = models.CharField(max_length=30, null=False)


class Collected(models.Model):
    u_Name = models.CharField(max_length=10, null=False)
    fl_Name = models.CharField(max_length=30, null=False)

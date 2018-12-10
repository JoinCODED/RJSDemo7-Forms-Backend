from django.db import models

# Create your models here.
class Person(models.Model):
	alias = models.CharField(max_length=120)
	description = models.CharField(max_length=120)
	email = models.EmailField()
from django.db import models

# Create your models here.

class Myuser(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
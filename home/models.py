from django.db import models

# Create your models here.

class Crime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
    occurence = models.CharField(max_length=500)
    action = models.CharField(max_length=500)
    type = models.CharField(max_length=50)
    # attachments = models.

    def __str__(self):
        return f"Crime(id={self.id}, type={self.type} )"

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
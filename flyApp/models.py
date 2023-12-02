from django.db import models

# Create your models here.

class Trip(models.Model):
    origin  = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)
    date = models.DateField()

    def __str__(self):
        return f"The trip from {self.origin} to {self.destination} departs on {self.date}"
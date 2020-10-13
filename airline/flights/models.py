from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length = 3)
    city = models.CharField(max_length = 60)

    def __str__(self):  # return a string representation of the object/record
        return f" city {self.code} {self.city}. "


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures" )
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals" )
    duration = models.IntegerField()

    def __str__(self):  # return a string representation of the object/record
        return f"{self.id}: {self.origin} to {self.destination} with duration of {self.duration} minutes."


from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor,on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=2, decimal_places=2)
    datetime = models.DateTimeField()

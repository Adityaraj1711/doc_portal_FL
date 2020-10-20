from django.db import models
import datetime


class Location(models.Model):
    location = models.CharField(default="", max_length=30, unique=True)

    def __str__(self):
        return self.location


class Procedure(models.Model):
    procedure = models.CharField(default="", max_length=30, unique=True)

    def __str__(self):
        return self.procedure


class GeneralEntry(models.Model):
    first_name = models.CharField(default="", max_length=100)
    last_name = models.CharField(default="", max_length=100, blank=True)
    mobile_number = models.IntegerField(max_length=10)
    address = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name + " " + self.last_name + " Location: " + self.location.location


class ProcedureForm(models.Model):
    first_name = models.CharField(default="", max_length=100)
    last_name = models.CharField(default="", max_length=100, blank=True)
    age = models.IntegerField()
    mobile_number = models.IntegerField(max_length=10)
    procedure = models.ForeignKey(Procedure, on_delete=models.PROTECT)
    dose_given = models.CharField(default="", max_length=3000)
    area_of_treatment = models.TextField(default="", max_length=3000)
    cost = models.CharField(default="", max_length=2000)
    result = models.TextField(default="", max_length=4000)
    remark = models.TextField(default="", max_length=4000, blank=True)
    no_of_session = models.IntegerField(default=0)
    settings_dose = models.TextField(default="", max_length=20000, blank=True)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.first_name + " " + self.last_name + " age: " + str(self.age) + " procedure: " + self.procedure.procedure + " ,treatment: " + self.area_of_treatment

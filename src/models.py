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
    SESSION_CHOICE = [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10")]
    no_of_session = models.CharField(default="0", choices=SESSION_CHOICE, max_length=10)
    settings_dose = models.CharField(default="", max_length=2000, blank=True)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.first_name + " " + self.last_name + " age: " + str(self.age) + " procedure: " + self.procedure.procedure + " ,treatment: " + self.area_of_treatment

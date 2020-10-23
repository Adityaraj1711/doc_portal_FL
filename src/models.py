from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField


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
    last_name = models.CharField(default="", max_length=100)
    mobile_number = models.CharField(default="", max_length=10)
    address = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'General Entry'
        verbose_name_plural = 'General Entry'

    def __str__(self):
        return self.first_name + " " + self.last_name + " Location: " + self.location.location


class ProcedureForm(models.Model):
    first_name = models.CharField(default="", max_length=100)
    last_name = models.CharField(default="", max_length=100)
    age = models.IntegerField(default="", max_length=2)
    mobile_number = models.CharField(default="", max_length=10)
    procedure = models.ForeignKey(Procedure, on_delete=models.PROTECT, blank=True)
    area_of_treatment = models.TextField(default="", max_length=3000, blank=True)
    cost = models.CharField(default="", max_length=2000, blank=True)
    result = models.TextField(default="", max_length=4000, blank=True)
    remark = models.TextField(default="", max_length=4000, blank=True)
    no_of_session = models.IntegerField(default=0)
    settings_dose = models.TextField(default="", max_length=20000)
    date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = 'Procedure Form'
        verbose_name_plural = 'Procedure Forms'

    def get_mobile_number(self):
        return len(self.mobile_number) == 10

    def __str__(self):
        return self.first_name + " " + self.last_name + " age: " + str(self.age) + " procedure: " + self.procedure.procedure + " ,treatment: " + self.area_of_treatment

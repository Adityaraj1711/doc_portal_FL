from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField


# class Location(models.Model):
#     location = models.CharField(default="", max_length=30, unique=True)
#
#     def __str__(self):
#         return self.location
#
#
# class Procedure(models.Model):
#     procedure = models.CharField(default="", max_length=30, unique=True)
#
#     def __str__(self):
#         return self.procedure
#
#
# class GeneralEntry(models.Model):
#     first_name = models.CharField(default="", max_length=100)
#     last_name = models.CharField(default="", max_length=100)
#     mobile_number = models.CharField(default="", max_length=10)
#     address = models.TextField()
#     date = models.DateTimeField(default=datetime.datetime.now)
#     location = models.ForeignKey(Location, on_delete=models.PROTECT)
#
#     class Meta:
#         verbose_name = 'General Entry'
#         verbose_name_plural = 'General Entry'
#
#     def __str__(self):
#         return self.first_name + " " + self.last_name + " Location: " + self.location.location
#

# class ProcedureForm(models.Model):
#     first_name = models.CharField(default="", max_length=100)
#     last_name = models.CharField(default="", max_length=100)
#     age = models.IntegerField(default="", max_length=2)
#     mobile_number = models.CharField(default="", max_length=10)
#     procedure = models.ForeignKey(Procedure, on_delete=models.PROTECT, blank=True)
#     area_of_treatment = models.TextField(default="", max_length=3000, blank=True)
#     cost = models.CharField(default="", max_length=2000, blank=True)
#     result = models.TextField(default="", max_length=4000, blank=True)
#     remark = models.TextField(default="", max_length=4000, blank=True)
#     no_of_session = models.IntegerField(default=0)
#     settings_dose = models.TextField(default="", max_length=20000)
#     date = models.DateTimeField(default=datetime.datetime.now)
#
#     class Meta:
#         verbose_name = 'Procedure Form'
#         verbose_name_plural = 'Procedure Forms'
#
#     def get_mobile_number(self):
#         return len(self.mobile_number) == 10
#
#     def __str__(self):
#         return self.first_name + " " + self.last_name + " age: " + str(self.age) + " procedure: " + self.procedure.procedure + " ,treatment: " + self.area_of_treatment


class AxisCompleteDetail(models.Model):
    state = models.CharField(default="", max_length=200, blank=True)
    final_city = models.CharField(default="", max_length=200, blank=True)
    account_ref = models.CharField(default="", max_length=200, blank=True)
    full_name = models.CharField(default="", max_length=200, blank=True)
    registration = models.CharField(default="", max_length=200, blank=True)
    manufacturer = models.CharField(default="", max_length=200, blank=True)
    chasis_number = models.CharField(default="", max_length=2000, blank=True)
    pos = models.FloatField(default=0, blank=True)
    bucket = models.CharField(default="", max_length=200, blank=True)
    address = models.CharField(default="", max_length=2000, blank=True)
    mobile_numer = models.CharField(default="", max_length=12, blank=True)
    emi_amount = models.FloatField(default=0, blank=True)
    final_emi_amount = models.FloatField(default=0, blank=True)
    emi_charges = models.FloatField(default=0, blank=True)
    total_overdue = models.FloatField(default=0, blank=True)
    total_od_charges = models.FloatField(default=0, blank=True)
    engine_number = models.CharField(default="", max_length=500, blank=True)
    cm_name = models.CharField(default="", max_length=200, blank=True)
    acm_name = models.CharField(default="", max_length=200, blank=True)

    def __str__(self):
        return self.manufacturer + ", reg: " + self.registration + ", name: " + self.full_name


class AxisCompleteDetail(models.Model):
    state = models.CharField(default="", max_length=200, blank=True, null=True)
    final_city = models.CharField(default="", max_length=200, blank=True, null=True)
    account_ref = models.CharField(default="", max_length=200, blank=True, null=True)
    full_name = models.CharField(default="", max_length=200, blank=True, null=True)
    registration = models.CharField(default="", max_length=200, blank=True, null=True)
    manufacturer = models.CharField(default="", max_length=200, blank=True, null=True)
    chasis_number = models.CharField(default="", max_length=2000, blank=True, null=True)
    pos = models.FloatField(default=0, blank=True, null=True)
    bucket = models.CharField(default="", max_length=200, blank=True, null=True)
    address = models.CharField(default="", max_length=2000, blank=True, null=True)
    mobile_numer = models.CharField(default="", max_length=12, blank=True, null=True)
    emi_amount = models.FloatField(default=0, blank=True, null=True)
    final_emi_amount = models.FloatField(default=0, blank=True, null=True)
    emi_charges = models.FloatField(default=0, blank=True, null=True)
    total_overdue = models.FloatField(default=0, blank=True, null=True)
    total_od_charges = models.FloatField(default=0, blank=True, null=True)
    engine_number = models.CharField(default="", max_length=500, blank=True, null=True)
    cm_name = models.CharField(default="", max_length=200, blank=True, null=True)
    acm_name = models.CharField(default="", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.manufacturer + ", reg: " + self.registration + ", name: " + self.full_name


class MahindraCompleteDetail(models.Model):
    hpa_no = models.CharField(default="", max_length=200, blank=True, null=True)
    name = models.CharField(default="", max_length=200, blank=True, null=True)
    brndes = models.CharField(default="", max_length=200, blank=True, null=True)
    rgndes = models.CharField(default="", max_length=200, blank=True, null=True)
    state = models.CharField(default="", max_length=200, blank=True, null=True)
    emp_name = models.CharField(default="", max_length=200, blank=True, null=True)
    outstand = models.CharField(default="", max_length=200, blank=True, null=True)
    age = models.CharField(default="", max_length=200, blank=True, null=True)
    bill1 = models.CharField(default="", max_length=200, blank=True, null=True)
    soh = models.CharField(default="", max_length=200, blank=True, null=True)
    assdes = models.CharField(default="", max_length=200, blank=True, null=True)
    status = models.CharField(default="", max_length=20, blank=True, null=True)
    branch = models.CharField(default="", max_length=200, blank=True, null=True)
    regno = models.CharField(default="", max_length=200, blank=True, null=True)
    engno = models.CharField(default="", max_length=200, blank=True, null=True)
    chsno = models.CharField(default="", max_length=200, blank=True, null=True)
    place = models.CharField(default="", max_length=200, blank=True, null=True)
    postoffice = models.CharField(default="", max_length=200, blank=True, null=True)
    road_name = models.CharField(default="", max_length=200, blank=True, null=True)
    landmark = models.CharField(default="", max_length=200, blank=True, null=True)
    city_village = models.CharField(default="", max_length=200, blank=True, null=True)
    state_code = models.CharField(default="", max_length=200, blank=True, null=True)
    district_code = models.CharField(default="", max_length=200, blank=True, null=True)
    taluk = models.CharField(default="", max_length=200, blank=True, null=True)
    website = models.CharField(default="", max_length=200, blank=True, null=True)
    pincode = models.CharField(default="", max_length=200, blank=True, null=True)
    office_phone_no = models.CharField(default="", max_length=200, blank=True, null=True)
    resi_telephone = models.CharField(default="", max_length=200, blank=True, null=True)
    mobile_no = models.CharField(default="", max_length=200, blank=True, null=True)
    pager_no = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_name = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_place = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_postoffice = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_road_name = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_landmark = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_city_village = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_state_des = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_district_des = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_taluk = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_pincode = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_office_phone_no = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_resi_telephone = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_mobile_no = models.CharField(default="", max_length=200, blank=True, null=True)
    cust_fatherName = models.CharField(default="", max_length=200, blank=True, null=True)
    priority_tag = models.CharField(default="", max_length=200, blank=True, null=True)
    october_handling_vertical_name = models.CharField(default="", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

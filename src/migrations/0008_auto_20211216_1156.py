# Generated by Django 3.1.2 on 2021-12-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0007_auto_20211209_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='MahindraCompleteDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hpa_no', models.CharField(blank=True, default='', max_length=200)),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('brndes', models.CharField(blank=True, default='', max_length=200)),
                ('rgndes', models.CharField(blank=True, default='', max_length=200)),
                ('state', models.CharField(blank=True, default='', max_length=200)),
                ('emp_name', models.CharField(blank=True, default='', max_length=200)),
                ('outstand', models.FloatField(blank=True, default=0)),
                ('age', models.FloatField(blank=True, default=0)),
                ('bill1', models.FloatField(blank=True, default=0)),
                ('soh', models.FloatField(blank=True, default=0)),
                ('assdes', models.CharField(blank=True, default='', max_length=200)),
                ('status', models.CharField(blank=True, default='', max_length=20)),
                ('branch', models.CharField(blank=True, default='', max_length=200)),
                ('regno', models.CharField(blank=True, default='', max_length=200)),
                ('engno', models.CharField(blank=True, default='', max_length=200)),
                ('chsno', models.CharField(blank=True, default='', max_length=200)),
                ('place', models.CharField(blank=True, default='', max_length=200)),
                ('postoffice', models.CharField(blank=True, default='', max_length=200)),
                ('road_name', models.CharField(blank=True, default='', max_length=200)),
                ('landmark', models.CharField(blank=True, default='', max_length=200)),
                ('city_village', models.CharField(blank=True, default='', max_length=200)),
                ('state_code', models.CharField(blank=True, default='', max_length=200)),
                ('district_code', models.CharField(blank=True, default='', max_length=200)),
                ('taluk', models.CharField(blank=True, default='', max_length=200)),
                ('website', models.CharField(blank=True, default='', max_length=200)),
                ('pincode', models.CharField(blank=True, default='', max_length=200)),
                ('office_phone_no', models.CharField(blank=True, default='', max_length=200)),
                ('resi_telephone', models.CharField(blank=True, default='', max_length=200)),
                ('mobile_no', models.CharField(blank=True, default='', max_length=200)),
                ('pager_no', models.CharField(blank=True, default='', max_length=200)),
                ('gu_name', models.CharField(blank=True, default='', max_length=200)),
                ('gu_place', models.CharField(blank=True, default='', max_length=200)),
                ('gu_postoffice', models.CharField(blank=True, default='', max_length=200)),
                ('gu_road_name', models.CharField(blank=True, default='', max_length=200)),
                ('gu_landmark', models.CharField(blank=True, default='', max_length=200)),
                ('gu_city_village', models.CharField(blank=True, default='', max_length=200)),
                ('gu_state_des', models.CharField(blank=True, default='', max_length=200)),
                ('gu_district_des', models.CharField(blank=True, default='', max_length=200)),
                ('gu_taluk', models.CharField(blank=True, default='', max_length=200)),
                ('gu_pincode', models.CharField(blank=True, default='', max_length=200)),
                ('gu_office_phone_no', models.CharField(blank=True, default='', max_length=200)),
                ('gu_resi_telephone', models.CharField(blank=True, default='', max_length=200)),
                ('gu_mobile_no', models.CharField(blank=True, default='', max_length=200)),
                ('cust_fatherName', models.CharField(blank=True, default='', max_length=200)),
                ('priority_tag', models.CharField(blank=True, default='', max_length=200)),
                ('october_handling_vertical_name', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='CompleteDetail',
            new_name='AxisCompleteDetail',
        ),
    ]

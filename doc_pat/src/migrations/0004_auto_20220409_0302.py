# Generated by Django 3.1.2 on 2022-04-08 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20220406_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='follow_up_days',
            field=models.IntegerField(choices=[(10, 10), (15, 15), (20, 20), (30, 30), (45, 45), (60, 60)], default=10, max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='M', max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='in_time',
            field=models.TimeField(default=datetime.datetime(2022, 4, 9, 3, 2, 18, 798948)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='seen_by_doctor',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]

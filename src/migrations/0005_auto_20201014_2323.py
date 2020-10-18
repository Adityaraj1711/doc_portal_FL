# Generated by Django 3.1.2 on 2020-10-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20201014_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalentry',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='procedureform',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='procedureform',
            name='setting1_dose',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='procedureform',
            name='setting2_dose',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='procedureform',
            name='setting3_dose',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]

# Generated by Django 3.2.5 on 2022-04-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp_scheduling_app', '0003_alter_attendancereport_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancereport',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schedulereportstaff',
            name='schedule_status',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.5 on 2022-04-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp_scheduling_app', '0005_alter_schedulereportstudent_schedule_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='fmc_token',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='students',
            name='fmc_token',
            field=models.TextField(default=''),
        ),
    ]

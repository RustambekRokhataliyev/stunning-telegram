# Generated by Django 4.1.5 on 2023-01-30 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_intransittrips_status_triphistories_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingtrips',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='upcomingtrips',
            name='date_start',
        ),
    ]

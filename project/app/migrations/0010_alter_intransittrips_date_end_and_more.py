# Generated by Django 4.1.5 on 2023-01-31 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_upcomingtrips_date_end_upcomingtrips_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intransittrips',
            name='date_end',
            field=models.TextField(max_length=255, null=True, verbose_name='date_end'),
        ),
        migrations.AlterField(
            model_name='intransittrips',
            name='date_start',
            field=models.TextField(max_length=255, null=True, verbose_name='date_start'),
        ),
    ]

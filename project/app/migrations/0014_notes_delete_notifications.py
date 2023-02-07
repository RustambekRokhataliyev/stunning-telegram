# Generated by Django 4.1.5 on 2023-02-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_id', models.TextField(null=True, verbose_name='load_id')),
                ('time', models.TextField(null=True, verbose_name='time_sent')),
                ('status', models.TextField(null=True, verbose_name='status')),
                ('comment', models.TextField(null=True, verbose_name='comment')),
            ],
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
    ]

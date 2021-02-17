# Generated by Django 3.1.4 on 2021-01-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_manager', '0004_auto_20210109_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='participant_registrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField(default='0')),
                ('participant_email', models.EmailField(max_length=254)),
                ('participant_name', models.CharField(default='Not provided', max_length=254)),
                ('participant_mobileno', models.IntegerField(default='0000000000')),
                ('participant_type', models.CharField(default='Single', max_length=6)),
                ('participant_total', models.IntegerField(default='1')),
            ],
        ),
    ]

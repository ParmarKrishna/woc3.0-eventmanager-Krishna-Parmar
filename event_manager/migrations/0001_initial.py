# Generated by Django 3.1.4 on 2021-01-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('From', models.DateTimeField()),
                ('To', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('poster_link', models.TextField()),
            ],
        ),
    ]

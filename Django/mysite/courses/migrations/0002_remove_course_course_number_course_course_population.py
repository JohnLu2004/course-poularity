# Generated by Django 4.1.3 on 2022-12-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_number',
        ),
        migrations.AddField(
            model_name='course',
            name='course_population',
            field=models.IntegerField(default=0),
        ),
    ]
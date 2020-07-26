# Generated by Django 3.0.8 on 2020-07-25 17:05

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.SlugField(default=course.models.random_course_code, unique=True),
        ),
    ]
# Generated by Django 5.1.1 on 2024-12-08 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('students', '0002_studentscoursel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentsCourseL',
            new_name='StudentsCourseList',
        ),
    ]
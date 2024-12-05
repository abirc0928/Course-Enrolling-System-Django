# Generated by Django 5.1.1 on 2024-12-05 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CourseSection', '0002_coursesection_teacher'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CourseSection.coursesection')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.students')),
            ],
        ),
    ]

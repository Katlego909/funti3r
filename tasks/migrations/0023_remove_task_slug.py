# Generated by Django 4.2.7 on 2024-01-10 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0022_task_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='slug',
        ),
    ]

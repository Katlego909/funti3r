# Generated by Django 4.2.7 on 2024-01-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_remove_task_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='experience',
            field=models.CharField(choices=[('entry', 'Entry Level'), ('mid', 'Mid Level'), ('senior', 'Senior Level')], default='entry', max_length=20),
        ),
    ]

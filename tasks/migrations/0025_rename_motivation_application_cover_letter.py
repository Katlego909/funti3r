# Generated by Django 4.2.7 on 2024-01-26 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0024_task_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='motivation',
            new_name='cover_letter',
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_task_changed_at_task_favorites_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='amount',
            field=models.FloatField(),
        ),
    ]

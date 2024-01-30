# Generated by Django 4.2.7 on 2023-12-29 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0016_rename_content_application_motivation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]

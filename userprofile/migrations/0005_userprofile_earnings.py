# Generated by Django 4.2.7 on 2024-01-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_userprofile_bio_userprofile_cell_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='earnings',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

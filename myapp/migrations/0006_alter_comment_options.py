# Generated by Django 4.2.7 on 2023-11-29 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_of_comment']},
        ),
    ]

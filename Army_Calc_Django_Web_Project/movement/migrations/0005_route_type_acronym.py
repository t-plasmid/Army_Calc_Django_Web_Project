# Generated by Django 2.2.25 on 2021-12-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movement', '0004_auto_20211224_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='route_type',
            name='acronym',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1_users', '0006_organisation_systemuser_organisation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='trained',
            field=models.BooleanField(default=False),
        ),
    ]

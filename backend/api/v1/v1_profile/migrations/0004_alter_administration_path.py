# Generated by Django 4.0.1 on 2022-02-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1_profile', '0003_administration_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='path',
            field=models.TextField(default=None, null=True),
        ),
    ]

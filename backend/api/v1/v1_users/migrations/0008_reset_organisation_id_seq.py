# Generated by Django 4.0.4 on 2022-08-29 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1_users', '0007_systemuser_trained'),
    ]

    operations = [
        migrations.RunSQL("""
        SELECT Setval('organisation_id_seq', (SELECT Max(id)
        FROM   organisation) + 1);
        """)
    ]
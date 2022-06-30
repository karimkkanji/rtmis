# Generated by Django 4.0.4 on 2022-06-23 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1_users', '0005_systemuser_deleted_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'organisation',
            },
        ),
        migrations.AddField(
            model_name='systemuser',
            name='organisation',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='user_organisation',
                to='v1_users.organisation'),
        ),
        migrations.CreateModel(
            name='OrganisationAttribute',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('type',
                 models.IntegerField(choices=[(1,
                                               'member'), (2,
                                                           'partnership')])),
                ('organisation',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='organisation_organisation_attribute',
                     to='v1_users.organisation')),
            ],
            options={
                'db_table': 'organisation_attribute',
                'unique_together': {('organisation', 'type')},
            },
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-26 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v1_forms', '0008_userforms'),
        ('v1_data', '0015_viewdataoptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingAnswerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.TextField(default=None, null=True)),
                ('value', models.BigIntegerField(default=None, null=True)),
                ('options', models.JSONField(default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=None, null=True)),
                ('created_by',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='pending_answer_history_created',
                     to=settings.AUTH_USER_MODEL)),
                ('pending_data',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='pending_data_answer_history',
                     to='v1_data.pendingformdata')),
                ('question',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='question_pending_answer_history',
                     to='v1_forms.questions')),
            ],
            options={
                'db_table': 'pending_answer_history',
            },
        ),
    ]

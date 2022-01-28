# Generated by Django 4.0.1 on 2022-01-28 13:12

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('v1_profile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('geo', models.JSONField(default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('administration',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='administration_form_data',
                                   to='v1_profile.administration')),
                ('created_by',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='form_data_created',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'data',
            },
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.TextField()),
                ('version', models.IntegerField(default=1)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False,
                                          unique=True)),
                ('type',
                 models.IntegerField(choices=[(1, 'County'), (2, 'National')],
                                     default=None, null=True)),
            ],
            options={
                'db_table': 'form',
            },
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.TextField()),
                ('form',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='form_question_group',
                                   to='v1_forms.forms')),
            ],
            options={
                'db_table': 'question_group',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('order', models.BigIntegerField(default=None, null=True)),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(
                    choices=[(1, 'Geo'), (2, 'Administration'), (3, 'Text'),
                             (4, 'Numeric'), (5, 'Option'),
                             (6, 'Multiple Option'), (7, 'Cascade'),
                             (8, 'Photo'), (9, 'Date')])),
                ('required', models.BooleanField(default=True)),
                ('rule', models.JSONField(default=None, null=True)),
                ('dependency', models.JSONField(default=None, null=True)),
                ('form',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='form_questions',
                                   to='v1_forms.forms')),
                ('question_group',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='question_group_question',
                                   to='v1_forms.questiongroup')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='QuestionOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('order', models.BigIntegerField(default=None, null=True)),
                ('code',
                 models.CharField(default=None, max_length=255, null=True)),
                ('name', models.TextField()),
                ('other', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('question',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='qustion_question_options',
                                   to='v1_forms.questions')),
            ],
            options={
                'db_table': 'option',
            },
        ),
        migrations.CreateModel(
            name='PendingFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('geo', models.JSONField(default=None, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('administration',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='administration_pending_form_data',
                                   to='v1_profile.administration')),
                ('created_by',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='pending_form_data_created',
                                   to=settings.AUTH_USER_MODEL)),
                ('data', models.ForeignKey(default=None, null=True,
                                           on_delete=django.db.models.deletion.CASCADE,
                                           related_name='pending_data_form_data',
                                           to='v1_forms.formdata')),
                ('form',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='pending_form_form_data',
                                   to='v1_forms.forms')),
            ],
            options={
                'db_table': 'pending_data',
            },
        ),
        migrations.CreateModel(
            name='PendingDataApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('status', models.IntegerField(
                    choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Rejected')],
                    default=1)),
                ('pending_data',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='pending_data_form_approval',
                                   to='v1_forms.pendingformdata')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='user_assigned_pending_data',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pending_data_approval',
            },
        ),
        migrations.CreateModel(
            name='PendingAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.BigIntegerField(default=None, null=True)),
                ('options', models.JSONField(default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='pending_answer_created',
                                   to=settings.AUTH_USER_MODEL)),
                ('pending_data',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='pending_data_answer',
                                   to='v1_forms.pendingformdata')),
                ('question',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='question_pending_answer',
                                   to='v1_forms.questions')),
            ],
            options={
                'db_table': 'pending_answer',
            },
        ),
        migrations.AddField(
            model_name='formdata',
            name='form',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='form_form_data', to='v1_forms.forms'),
        ),
        migrations.AddField(
            model_name='formdata',
            name='updated_by',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='form_data_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FormApprovalRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('administration',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='administration_form_approval',
                                   to='v1_profile.administration')),
                ('form',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='form_form_approval_rule',
                                   to='v1_forms.forms')),
                ('levels',
                 models.ManyToManyField(related_name='levels_form_approval',
                                        to='v1_profile.Levels')),
            ],
            options={
                'db_table': 'form_approval_rule',
            },
        ),
        migrations.CreateModel(
            name='FormApprovalAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('administration',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='administration_data_approval',
                                   to='v1_profile.administration')),
                ('form',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='form_data_approval',
                                   to='v1_forms.forms')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='user_data_approval',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'form_approval_assignment',
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.BigIntegerField(default=None, null=True)),
                ('options', models.JSONField(default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='answer_created',
                                   to=settings.AUTH_USER_MODEL)),
                ('data',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='data_answer',
                                   to='v1_forms.formdata')),
                ('question',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='question_answer',
                                   to='v1_forms.questions')),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='AnswerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.BigIntegerField(default=None, null=True)),
                ('options', models.JSONField(default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='answer_history_created',
                    to=settings.AUTH_USER_MODEL)),
                ('data',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='data_answer_history',
                                   to='v1_forms.formdata')),
                ('question',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='question_answer_history',
                                   to='v1_forms.questions')),
            ],
            options={
                'db_table': 'answer_history',
            },
        ),
    ]

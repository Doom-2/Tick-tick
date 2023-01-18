# Generated by Django 4.1.4 on 2023-01-17 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('status', models.PositiveSmallIntegerField(
                    choices=[(1, 'To Do'), (2, 'In progress'), (3, 'Done'), (4, 'Archived')], default=1,
                    verbose_name='status')),
                ('priority', models.PositiveSmallIntegerField(
                    choices=[(1, 'To Do'), (2, 'In progress'), (3, 'Done'), (4, 'Archived')], default=2,
                    verbose_name='priority')),
                ('deadline', models.DateTimeField(auto_now_add=True, verbose_name='deadline')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goals.goalcategory',
                                               verbose_name='category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL,
                                           verbose_name='author')),
            ],
            options={
                'verbose_name': 'Goal',
                'verbose_name_plural': 'Goals',
            },
        ),
        migrations.CreateModel(
            name='GoalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('goal',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goal', verbose_name='goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                           verbose_name='author')),
            ],
            options={
                'verbose_name': 'GoalComment',
                'verbose_name_plural': 'GoalComments',
            },
        ),
    ]

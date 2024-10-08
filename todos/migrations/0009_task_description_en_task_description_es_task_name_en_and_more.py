# Generated by Django 5.0.6 on 2024-10-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_remove_task_assigned_to_remove_subtask_assigned_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description_en',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_es',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='name_es',
            field=models.CharField(max_length=150, null=True),
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-20 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_text',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_date',
        ),
        migrations.AddField(
            model_name='task',
            name='create_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='task',
            name='deadline_date',
            field=models.DateField(null=True),
        ),
    ]
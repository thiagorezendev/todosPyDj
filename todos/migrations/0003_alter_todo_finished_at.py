# Generated by Django 5.0.6 on 2024-07-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='finished_at',
            field=models.DateField(null=True),
        ),
    ]

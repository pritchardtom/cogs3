# Generated by Django 2.0.2 on 2018-06-20 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0025_remove_project_institution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='funding_source',
        ),
    ]
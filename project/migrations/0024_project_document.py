# Generated by Django 2.0.2 on 2018-06-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_auto_20180524_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/%M/', verbose_name='Upload Supporting Documents'),
        ),
    ]

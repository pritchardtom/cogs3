# Generated by Django 2.0.2 on 2018-05-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_merge_20180523_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='notes',
            field=models.TextField(blank=True, help_text='Internal project notes', max_length=512, verbose_name='Notes'),
        ),
    ]
# Generated by Django 2.0.2 on 2018-09-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0017_auto_20180906_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='needs_user_approval',
            field=models.BooleanField(default=True),
        ),
    ]
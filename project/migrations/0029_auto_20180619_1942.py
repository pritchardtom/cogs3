# Generated by Django 2.0.2 on 2018-06-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0028_project_gid_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='previous_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Awaiting Approval'), (2, 'Approved'), (3, 'Declined'), (4, 'Revoked'), (5, 'Suspended'), (6, 'Closed')], default=1, verbose_name='Previous Status'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Awaiting Approval'), (2, 'Approved'), (3, 'Declined'), (4, 'Revoked'), (5, 'Suspended'), (6, 'Closed')], default=1, verbose_name='Current Status'),
        ),
    ]

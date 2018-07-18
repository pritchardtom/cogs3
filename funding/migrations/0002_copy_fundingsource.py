# Generated by Django 2.0.2 on 2018-07-17 11:28

from django.db import migrations


def forwards(apps, schema_editor):
    # Copy the funding_source table
    Project = apps.get_model('project', 'Project')
    ProjectFundingSource = apps.get_model('project', 'ProjectFundingSource')
    FundingBody = apps.get_model('funding', 'FundingBody')
    FundingSource = apps.get_model('funding', 'FundingSource')

    for pfs in ProjectFundingSource.objects.all():
        fb = FundingBody(
            name=pfs.name,
            description=pfs.description,
        )
        fb.save()

    for p in Project.objects.all():
        # Create a funding source matching the old funding source
        fb = FundingBody.objects.get(id=p.funding_source.id)
        fs = FundingSource(
            title='',
            identifier='',
            created_by=p.tech_lead,
            funding_body=fb,
        )
        fs.save()
        # Save it to the ManyToManyField
        p.attributions.add(fs)


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
        ('project', '0037_auto_20180717_1128'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]

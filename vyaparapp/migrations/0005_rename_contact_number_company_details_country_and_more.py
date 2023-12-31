# Generated by Django 4.2.3 on 2023-10-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0004_staff_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_details',
            old_name='contact_number',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='company_details',
            old_name='business_name',
            new_name='gst_type',
        ),
        migrations.RenameField(
            model_name='company_details',
            old_name='company_email',
            new_name='pan_number',
        ),
        migrations.RemoveField(
            model_name='company_details',
            name='company_type',
        ),
        migrations.RemoveField(
            model_name='company_details',
            name='industry_type',
        ),
        migrations.AddField(
            model_name='company_details',
            name='End_date',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company_details',
            name='start_date',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
    ]

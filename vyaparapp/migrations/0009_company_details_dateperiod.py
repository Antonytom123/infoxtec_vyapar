# Generated by Django 4.2.3 on 2023-10-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0008_company_details_action_staff_details_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_details',
            name='dateperiod',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

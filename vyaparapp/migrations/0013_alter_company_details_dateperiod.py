# Generated by Django 4.2.3 on 2023-10-15 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0012_company_details_company_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='dateperiod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.payment_terms'),
        ),
    ]

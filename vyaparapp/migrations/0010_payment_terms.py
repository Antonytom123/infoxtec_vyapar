# Generated by Django 4.2.3 on 2023-10-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0009_company_details_dateperiod'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_terms_number', models.IntegerField(blank=True, null=True)),
                ('payment_terms_value', models.CharField(blank=True, max_length=100, null=True)),
                ('days', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

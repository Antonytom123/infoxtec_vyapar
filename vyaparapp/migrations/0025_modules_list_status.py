# Generated by Django 4.2.3 on 2023-10-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0024_modules_list_update_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules_list',
            name='status',
            field=models.CharField(default='New', max_length=100, null=True),
        ),
    ]

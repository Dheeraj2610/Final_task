# Generated by Django 4.1.5 on 2023-02-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0014_alter_employeemodel_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='nature_of_leave',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

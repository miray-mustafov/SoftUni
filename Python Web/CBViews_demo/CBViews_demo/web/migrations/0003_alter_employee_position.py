# Generated by Django 4.1.3 on 2022-11-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employeebasic_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('default', 'default'), ('junior', 'junior'), ('mid', 'mid'), ('senior', 'senior')], default='default', max_length=7),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='experience',
            field=models.CharField(choices=[('employee', 'موظف'), ('interview', 'مقابلة'), ('coop', 'تدريب')], max_length=128),
        ),
    ]
# Generated by Django 3.1.6 on 2021-03-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210301_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerprofile',
            name='company_name',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
    ]

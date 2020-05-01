# Generated by Django 3.1.6 on 2021-02-28 19:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketplace', '0006_auto_20210228_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='saves',
        ),
        migrations.AddField(
            model_name='listing',
            name='interview_requests',
            field=models.ManyToManyField(blank=True, related_name='interviews', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-30 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0002_auto_20201030_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='social_video',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='timer_last_active',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 20, 48, 31, 520695)),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-30 17:21

import datetime
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0003_auto_20201030_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='social_image',
            field=models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', storage=django.core.files.storage.FileSystemStorage(location=''), upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='timer_last_active',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 22, 51, 25, 197248)),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-24 08:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_subject_user_subject_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/subject/'),
            preserve_default=False,
        ),
    ]
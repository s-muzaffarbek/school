# Generated by Django 5.1.3 on 2024-12-21 05:17

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='teacher',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='test',
            name='options',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(default=datetime.datetime(2024, 12, 21, 5, 17, 20, 564924, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentresult',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 12, 21, 5, 17, 26, 837540, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='a',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='b',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='c',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='d',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='e',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher')], max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='classroom',
            field=models.ManyToManyField(related_name='classroom', to='core.classroom'),
        ),
    ]
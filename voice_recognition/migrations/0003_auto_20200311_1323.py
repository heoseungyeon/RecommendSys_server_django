# Generated by Django 3.0.4 on 2020-03-11 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice_recognition', '0002_auto_20200311_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
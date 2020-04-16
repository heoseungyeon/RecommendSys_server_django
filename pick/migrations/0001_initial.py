# Generated by Django 2.1 on 2020-04-16 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user_pw', models.CharField(blank=True, max_length=150, null=True)),
                ('user_nm', models.CharField(blank=True, max_length=50, null=True)),
                ('user_email', models.CharField(blank=True, max_length=100, null=True)),
                ('posting_cnt', models.IntegerField(blank=True, null=True)),
                ('following_cnt', models.IntegerField(blank=True, null=True)),
                ('follower_cnt', models.IntegerField(blank=True, null=True)),
                ('decription', models.TextField(blank=True, null=True)),
                ('age', models.CharField(blank=True, max_length=45, null=True)),
                ('sex', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserPick',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('place_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'user_pick',
                'managed': False,
            },
        ),
    ]
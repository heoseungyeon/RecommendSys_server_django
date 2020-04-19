# Generated by Django 2.1 on 2020-04-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImageM',
            fields=[
                ('ctgr_mid', models.AutoField(primary_key=True, serialize=False)),
                ('ctgr_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'category_image_m',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryImageS',
            fields=[
                ('ctgr_sid', models.AutoField(primary_key=True, serialize=False)),
                ('ctgr_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'category_image_s',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryL',
            fields=[
                ('ctgr_lid', models.AutoField(primary_key=True, serialize=False)),
                ('ctgr_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'category_l',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryTextM',
            fields=[
                ('ctgr_id', models.AutoField(primary_key=True, serialize=False)),
                ('ctgr_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'category_text_m',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryTextS',
            fields=[
                ('ctgr_id', models.AutoField(primary_key=True, serialize=False)),
                ('ctgr_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'category_text_s',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImageMScore',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'image_m_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImageSScore',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_idx', models.IntegerField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'image_s_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TextMScore',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'text_m_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TextSScore',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'text_s_score',
                'managed': False,
            },
        ),
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
            name='UserFollow',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_follow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserLScore',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_l_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserPlaceHistory',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('place_id', models.CharField(blank=True, max_length=100, null=True)),
                ('context', models.TextField(blank=True, null=True)),
                ('img_cnt', models.IntegerField(blank=True, null=True)),
                ('like_cnt', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('tag_1', models.CharField(blank=True, max_length=45, null=True)),
                ('tag_2', models.CharField(blank=True, max_length=45, null=True)),
                ('tag_3', models.CharField(blank=True, max_length=45, null=True)),
                ('tag_4', models.CharField(blank=True, max_length=45, null=True)),
                ('tag_5', models.CharField(blank=True, max_length=45, null=True)),
                ('tag_6', models.CharField(blank=True, max_length=45, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_place_history',
                'managed': False,
            },
        ),
    ]

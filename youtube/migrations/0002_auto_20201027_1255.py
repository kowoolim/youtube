# Generated by Django 3.1.2 on 2020-10-27 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('In_idx', models.AutoField(primary_key=True, serialize=False)),
                ('view_sub', models.IntegerField(default=0)),
                ('video_nums', models.IntegerField(default=0)),
                ('male', models.IntegerField(default=0)),
                ('multisex', models.IntegerField(default=0)),
                ('contents', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Youtube_in',
        ),
        migrations.DeleteModel(
            name='Youtube_out',
        ),
    ]

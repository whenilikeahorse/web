# Generated by Django 2.1.8 on 2019-08-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190804_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.TextField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.TextField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='major',
            field=models.TextField(blank=True, max_length=10),
        ),
    ]
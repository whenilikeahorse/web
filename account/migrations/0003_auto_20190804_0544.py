# Generated by Django 2.1.8 on 2019-08-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.TextField(blank=True, max_length=20),
        ),
    ]

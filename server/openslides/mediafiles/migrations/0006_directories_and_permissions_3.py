# Generated by Django 2.2.2 on 2019-06-28 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_auto_20190119_1447"),
        ("mediafiles", "0005_directories_and_permissions_2"),
    ]

    operations = [
        migrations.RemoveField(model_name="mediafile", name="hidden"),
        migrations.RemoveField(model_name="mediafile", name="uploader"),
    ]

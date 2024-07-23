# Generated by Django 5.0.7 on 2024-07-18 21:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FileSystem", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="id",
        ),
        migrations.AddField(
            model_name="file",
            name="full_path",
            field=models.CharField(
                default="name", max_length=255, primary_key=True, serialize=False
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="file",
            name="name",
            field=models.CharField(default="nametest", max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_profile_password_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="Blood_Group",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

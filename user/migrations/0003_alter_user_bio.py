# Generated by Django 4.1.2 on 2022-10-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_bio_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]

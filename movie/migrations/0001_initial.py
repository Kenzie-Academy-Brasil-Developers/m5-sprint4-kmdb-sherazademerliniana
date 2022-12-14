# Generated by Django 4.1.2 on 2022-10-24 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("genre", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(max_length=10)),
                ("premiere", models.DateField()),
                ("classification", models.PositiveIntegerField()),
                ("synopsis", models.TextField()),
                (
                    "genres",
                    models.ManyToManyField(related_name="genres", to="genre.genre"),
                ),
            ],
        ),
    ]

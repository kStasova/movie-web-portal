# Generated by Django 4.1.2 on 2023-04-18 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "tmdb_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("apiDb", models.CharField(max_length=255)),
                ("posterPath", models.CharField(max_length=255, null=True)),
                ("title", models.CharField(max_length=255)),
                ("releaseYear", models.DateField(null=True)),
                ("popularity", models.FloatField(null=True)),
                ("video", models.CharField(max_length=255, null=True)),
                ("genres", models.ManyToManyField(to="movie_web_app.genre")),
            ],
        ),
        migrations.CreateModel(
            name="VideoObject",
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
                ("model", models.CharField(max_length=255)),
                ("label", models.CharField(max_length=255)),
                ("maxConf", models.DecimalField(decimal_places=5, max_digits=6)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie_web_app.movie",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PosterObject",
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
                ("model", models.CharField(max_length=255)),
                ("label", models.CharField(max_length=255)),
                ("conf", models.DecimalField(decimal_places=5, max_digits=6)),
                ("box", models.JSONField()),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie_web_app.movie",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-21 11:30

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Footer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=500)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from="title"
                    ),
                ),
                ("introduction", models.TextField(blank=True, max_length=500)),
                ("address", models.CharField(blank=True, max_length=500)),
                ("email", models.CharField(blank=True, max_length=500)),
                ("phone", models.CharField(blank=True, max_length=500)),
                ("economy", models.CharField(blank=True, max_length=500)),
            ],
            options={"abstract": False},
        )
    ]

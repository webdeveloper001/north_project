# Generated by Django 2.2.4 on 2019-08-12 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wagtailredirects", "0006_redirect_increase_max_length"),
        ("wagtailforms", "0003_capitalizeverbose"),
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticlePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                )
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        ),
        migrations.RenameModel(old_name="HomePage", new_name="StandardPage"),
    ]

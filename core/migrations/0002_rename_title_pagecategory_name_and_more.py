# Generated by Django 4.1 on 2022-08-14 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pagecategory",
            old_name="title",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="content",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="game",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="image",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="intro",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="is_featured",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="is_published",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="note",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="seo_title",
        ),
        migrations.RemoveField(
            model_name="pagecategory",
            name="table",
        ),
        migrations.AddField(
            model_name="page",
            name="game",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="pages",
                to="core.game",
            ),
        ),
    ]

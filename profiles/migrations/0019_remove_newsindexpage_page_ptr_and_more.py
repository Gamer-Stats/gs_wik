# Generated by Django 4.0.6 on 2022-07-17 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_categories_newsindexpage_newspage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='new_category',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='NewsIndexPage',
        ),
        migrations.DeleteModel(
            name='NewsPage',
        ),
    ]

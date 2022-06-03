# Generated by Django 4.0.4 on 2022-06-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_wikicategory_parent_alter_wiki_related'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikicategory',
            name='cat_level',
            field=models.CharField(blank=True, choices=[('c', 'Country'), ('t', 'Teams'), ('p', 'Players')], max_length=1, null=True),
        ),
    ]

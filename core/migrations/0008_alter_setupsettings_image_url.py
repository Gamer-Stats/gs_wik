# Generated by Django 4.0.4 on 2022-06-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_setupsettings_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setupsettings',
            name='image_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-31 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20211025_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

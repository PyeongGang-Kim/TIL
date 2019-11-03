# Generated by Django 2.2.6 on 2019-11-02 13:59

import articles.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20191015_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=articles.models.articles_image_path),
        ),
    ]

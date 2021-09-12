# Generated by Django 3.2.4 on 2021-09-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_productcolor_product_type_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_image_banner',
            new_name='event_image_banner_name',
        ),
        migrations.AddField(
            model_name='event',
            name='event_image_banner_path',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]

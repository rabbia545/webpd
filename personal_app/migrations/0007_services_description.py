# Generated by Django 4.1.3 on 2022-12-06 13:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_app', '0006_testmonials_remove_services_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=ckeditor.fields.RichTextField(default='xyz'),
        ),
    ]

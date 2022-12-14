# Generated by Django 4.1.3 on 2022-12-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_app', '0003_rename_interest_interests_rename_service_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('icon', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]
# Generated by Django 4.2.8 on 2023-12-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
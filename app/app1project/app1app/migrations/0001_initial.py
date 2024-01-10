# Generated by Django 4.2.8 on 2023-12-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200)),
                ('movie_name', models.CharField(max_length=200)),
                ('singer', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]

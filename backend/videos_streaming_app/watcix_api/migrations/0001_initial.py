# Generated by Django 3.0.6 on 2020-05-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uploader_name', models.CharField(max_length=50)),
                ('Name_of_movie', models.CharField(max_length=50)),
                ('Genre_of_movie', models.TextField()),
                ('Duration_of_movie', models.IntegerField(default=1000)),
                ('Rating', models.IntegerField(default=10)),
                ('Thumbnail', models.ImageField(upload_to='movies/Images')),
                ('Video_clip', models.FileField(upload_to='movies')),
            ],
        ),
    ]

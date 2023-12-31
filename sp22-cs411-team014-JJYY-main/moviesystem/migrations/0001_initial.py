# Generated by Django 3.2.5 on 2022-04-01 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('directorID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('preferredGenres', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField(max_length=45)),
                ('adultStatus', models.BooleanField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('releaseDate', models.CharField(max_length=15)),
                ('duration', models.IntegerField(max_length=45)),
                ('genre', models.CharField(max_length=45)),
                ('ratingFromTomato', models.FloatField(max_length=45)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='directors', to='moviesystem.director')),
            ],
        ),
    ]

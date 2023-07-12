# Generated by Django 3.2.5 on 2022-04-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesystem', '0003_auto_20220401_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='birthYear',
            field=models.IntegerField(default=1997),
        ),
        migrations.AddField(
            model_name='director',
            name='birthYear',
            field=models.IntegerField(default=1960),
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=120),
        ),
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='source',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='adultStatus',
            field=models.CharField(max_length=20),
        ),
    ]

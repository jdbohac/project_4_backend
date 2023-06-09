# Generated by Django 4.2 on 2023-04-11 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('release_date', models.CharField(max_length=32)),
                ('img', models.TextField()),
                ('game_genre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('tag', models.CharField(max_length=32)),
                ('availability', models.CharField(max_length=32)),
                ('time_zone', models.CharField(max_length=32)),
                ('skill_level', models.CharField(max_length=32)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lanbuddy_api.game')),
            ],
        ),
    ]

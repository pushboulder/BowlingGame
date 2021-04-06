# Generated by Django 3.1.7 on 2021-04-06 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bowling', '0002_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameRoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bowling.game')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bowling.roll')),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2022-10-03 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='season',
            old_name='for_film',
            new_name='film',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='season_number',
            new_name='number',
        ),
    ]

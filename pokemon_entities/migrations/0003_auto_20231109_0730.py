# Generated by Django 3.1.14 on 2023-11-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-12 07:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nd', '0002_gallery_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FileField(upload_to='static/images/uploads/gallery'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Deserts', 'Deserts'), ('Wine Card', 'Wine Card'), ('Drinks & Tea', 'Drinks & Tea')], max_length=200, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.FileField(upload_to='static/images/uploads/menu'),
        ),
    ]

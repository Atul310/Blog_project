# Generated by Django 4.1.7 on 2023-08-27 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile_pics/', upload_to='profile_pics'),
        ),
    ]

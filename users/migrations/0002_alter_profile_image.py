# Generated by Django 4.1.7 on 2023-08-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
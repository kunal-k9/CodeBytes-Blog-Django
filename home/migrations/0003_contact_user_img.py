# Generated by Django 5.0.1 on 2024-02-17 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user_img',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
    ]

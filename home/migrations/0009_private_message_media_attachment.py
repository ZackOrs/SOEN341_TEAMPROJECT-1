# Generated by Django 2.1.7 on 2019-03-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_private_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='private_message',
            name='media_attachment',
            field=models.ImageField(blank=True, default='default.png', upload_to='site_media'),
        ),
    ]

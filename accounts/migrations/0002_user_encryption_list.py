# Generated by Django 2.1.7 on 2019-03-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_encryption_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile_name', models.CharField(max_length=255)),
                ('encryption_key', models.CharField(max_length=255)),
                ('enc_keys_notes', models.TextField(max_length=255)),
            ],
        ),
    ]

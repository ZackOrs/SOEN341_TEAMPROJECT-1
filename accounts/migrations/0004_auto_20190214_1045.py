# Generated by Django 2.1.5 on 2019-02-14 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190214_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='user_first_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='user_last_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_password',
            field=models.CharField(default='**********', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_profile_name',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]

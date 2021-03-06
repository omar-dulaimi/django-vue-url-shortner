# Generated by Django 4.0.3 on 2022-04-10 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0003_alter_userurl_uniqueid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userurl',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userurl',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

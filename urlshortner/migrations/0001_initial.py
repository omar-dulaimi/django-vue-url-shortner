# Generated by Django 4.0.3 on 2022-04-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originalUrl', models.CharField(max_length=2048)),
                ('uniqueId', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]

# Generated by Django 5.0 on 2024-06-26 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='usernamefield',
        ),
    ]
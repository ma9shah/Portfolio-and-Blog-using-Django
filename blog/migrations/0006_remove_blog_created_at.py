# Generated by Django 2.2.2 on 2019-06-17 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190617_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
    ]

# Generated by Django 2.0.5 on 2020-01-07 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_commment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commment',
            new_name='Comment',
        ),
    ]

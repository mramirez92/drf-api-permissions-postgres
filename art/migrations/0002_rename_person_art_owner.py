# Generated by Django 4.1.5 on 2023-02-01 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art',
            old_name='person',
            new_name='owner',
        ),
    ]

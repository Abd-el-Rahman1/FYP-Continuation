# Generated by Django 3.1.5 on 2021-02-18 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20210219_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='sponsor',
            new_name='sponsors',
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_auto_20210218_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

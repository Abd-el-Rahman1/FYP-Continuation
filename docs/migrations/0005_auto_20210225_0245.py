# Generated by Django 3.1.5 on 2021-02-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_auto_20210223_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

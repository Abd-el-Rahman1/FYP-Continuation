# Generated by Django 3.1.5 on 2021-02-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210216_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.CharField(max_length=250),
        ),
    ]

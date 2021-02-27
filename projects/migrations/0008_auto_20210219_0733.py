# Generated by Django 3.1.5 on 2021-02-18 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20210217_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='sponsor',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

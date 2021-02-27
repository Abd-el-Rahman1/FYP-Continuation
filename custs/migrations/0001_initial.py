# Generated by Django 3.1.5 on 2021-02-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('age', models.IntegerField(default=0, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('productID', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('source', models.CharField(choices=[('Blog', 'Blog'), ('Social media', 'Social media'), ('Friend', 'Friend'), ('Google search', 'Google search'), ('Product package', 'Product package'), ('Company Employee', 'Company Employee')], max_length=250, null=True)),
                ('problem', models.CharField(max_length=1000)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

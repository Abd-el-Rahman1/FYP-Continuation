# Generated by Django 3.1.5 on 2021-02-13 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0003_auto_20210214_0221'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=1000)),
                ('category', models.CharField(blank=True, max_length=150)),
                ('probability', models.DecimalField(decimal_places=1, max_digits=2)),
                ('impact', models.DecimalField(decimal_places=1, max_digits=2)),
                ('priority', models.CharField(choices=[('Very High', 'Very High'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'), ('Very Low', 'Very Low')], max_length=30, null=True)),
                ('effect', models.TextField(blank=True, max_length=1000)),
                ('rrp', models.TextField(blank=True, max_length=1000)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Inprogress', 'Inprogress'), ('Closed', 'Closed')], max_length=30, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(blank=True, null=True)),
                ('dateFinished', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('pName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project')),
            ],
        ),
    ]

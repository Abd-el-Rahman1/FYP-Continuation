# Generated by Django 3.1.5 on 2021-02-22 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=250)),
                ('areaAudited', models.TextField()),
                ('NCR_or_OFI', models.CharField(choices=[('NCR', 'NCR'), ('OFI', 'OFI')], max_length=30)),
                ('comment', models.TextField(blank=True, null=True)),
                ('closed', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now_add=True)),
                ('dateFinished', models.DateTimeField(blank=True, null=True)),
                ('auditee', models.ManyToManyField(related_name='auditees', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

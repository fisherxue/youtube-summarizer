# Generated by Django 2.1.5 on 2019-01-27 15:45

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summarizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_id', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('timestamp', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), size=None)),
                ('summary', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('time_summary_dict', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
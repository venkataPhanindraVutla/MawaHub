# Generated by Django 5.0.7 on 2024-10-31 11:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-score', '-date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('question', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]

# Generated by Django 5.2.3 on 2025-07-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('lastname', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
            ],
        ),
    ]

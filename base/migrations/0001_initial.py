# Generated by Django 4.2.1 on 2023-05-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('json', models.JSONField(max_length=5000)),
                ('private_key', models.CharField(max_length=200)),
            ],
        ),
    ]

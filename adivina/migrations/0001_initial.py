# Generated by Django 4.2.7 on 2023-11-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adivina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_secret', models.IntegerField()),
                ('attempts', models.IntegerField(default=0)),
            ],
        ),
    ]

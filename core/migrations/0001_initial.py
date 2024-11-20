# Generated by Django 5.1.3 on 2024-11-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255, verbose_name='Название города')),
                ('latitude', models.FloatField(verbose_name='Географическая широта')),
                ('longitude', models.FloatField(verbose_name='Географическая долгота')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'db_table': 'cities',
                'ordering': ['city_name'],
            },
        ),
    ]
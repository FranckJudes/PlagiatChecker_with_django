# Generated by Django 3.2.20 on 2023-12-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagiatLocal', '0009_auto_20231230_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomdoc', models.CharField(max_length=200)),
                ('nomtest', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('ratio', models.IntegerField(max_length=200)),
                ('idtest', models.IntegerField(max_length=200)),
            ],
        ),
    ]

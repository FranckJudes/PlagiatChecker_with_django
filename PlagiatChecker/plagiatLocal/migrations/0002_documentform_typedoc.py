# Generated by Django 3.2.20 on 2023-11-28 00:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plagiatLocal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentform',
            name='typedoc',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='type de fichie'),
            preserve_default=False,
        ),
    ]

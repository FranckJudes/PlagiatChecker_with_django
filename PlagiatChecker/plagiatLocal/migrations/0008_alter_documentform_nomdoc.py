# Generated by Django 3.2.20 on 2023-11-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagiatLocal', '0007_alter_documentform_nomdoc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentform',
            name='nomdoc',
            field=models.FileField(null=True, upload_to='public'),
        ),
    ]

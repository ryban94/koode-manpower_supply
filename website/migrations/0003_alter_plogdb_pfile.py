# Generated by Django 3.2.10 on 2023-08-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_plogdb_pfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plogdb',
            name='pfile',
            field=models.ImageField(blank=True, null=True, upload_to='pf'),
        ),
    ]

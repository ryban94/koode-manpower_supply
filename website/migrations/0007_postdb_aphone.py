# Generated by Django 3.2.10 on 2023-08-15 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_postdb_ausername'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdb',
            name='aphone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

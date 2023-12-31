# Generated by Django 3.2.10 on 2023-08-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_plogdb_pfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='clogdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfname', models.CharField(blank=True, max_length=100, null=True)),
                ('clname', models.CharField(blank=True, max_length=500, null=True)),
                ('cbirthday', models.CharField(blank=True, max_length=500, null=True)),
                ('cgender', models.CharField(blank=True, max_length=500, null=True)),
                ('cemail', models.CharField(blank=True, max_length=500, null=True)),
                ('cphone', models.IntegerField(blank=True, null=True)),
                ('ccity', models.CharField(blank=True, max_length=500, null=True)),
                ('cpincode', models.IntegerField(blank=True, null=True)),
                ('cid', models.CharField(blank=True, max_length=500, null=True)),
                ('cfile', models.ImageField(blank=True, null=True, upload_to='image')),
                ('cpassword', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='plogdb',
            name='pfile',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]

# Generated by Django 4.1.1 on 2023-05-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_logtable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='login_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='logtable',
            name='logout_time',
            field=models.DateTimeField(),
        ),
    ]

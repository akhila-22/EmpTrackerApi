# Generated by Django 4.1.1 on 2023-05-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_logtable_logout_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='logout_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

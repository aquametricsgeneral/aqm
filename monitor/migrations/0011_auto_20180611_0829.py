# Generated by Django 2.0.4 on 2018-06-11 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0010_auto_20180611_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertsetting',
            name='alert',
            field=models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF')], default='ON', max_length=10),
        ),
    ]

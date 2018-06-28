# Generated by Django 2.0.4 on 2018-06-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20180610_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertsetting',
            name='id',
        ),
        migrations.AlterField(
            model_name='alertsetting',
            name='sensor',
            field=models.CharField(choices=[('EnvTemp', 'Environment Temp'), ('EnvHumidity', 'Humidity'), ('WaterTempFishTank', 'Fish Tank Water Temp'), ('WaterTempSumpTank', 'Sump Tank Water Temp'), ('WaterPH', 'Water pH'), ('WaterLevelLow', 'Low Water Level'), ('WaterLevelFull', 'Full Water Level'), ('IsFilling', 'Water Filling'), ('WaterFlowFishTank', 'Fish Tank Water Flow'), ('WaterFlowMain', 'Main Water Flow'), ('WaterFlowVertGrow', 'Vertical Water Flow'), ('WaterFlowHorizGrow', 'Horizontal Water Flow')], default='EnvTemp', max_length=30, primary_key=True, serialize=False),
        ),
    ]

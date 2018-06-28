# Generated by Django 2.0.4 on 2018-06-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0019_auto_20180611_1355'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WaterLevelHigh',
            new_name='WaterLevelFull',
        ),
        migrations.AlterField(
            model_name='alertsetting',
            name='sensor',
            field=models.CharField(choices=[('envtemp', 'EnvTemp'), ('envhumidity', 'EnvHumidity'), ('watertempfishtank', 'WaterTempFishTank'), ('watertempsumptank', 'WaterTempSumpTank'), ('waterph', 'WaterPH'), ('isfilling', 'IsFilling'), ('waterlevellow', 'WaterLevelLow'), ('waterlevelfull', 'WaterLevelFull'), ('waterflowfishtank', 'WaterFlowFishTank'), ('waterflowmain', 'WaterFlowMain'), ('waterflowvertgrow', 'WaterFlowVertGrow'), ('waterflowhorizgrow', 'WaterFlowHorizGrow')], default='envtemp', max_length=30, primary_key=True, serialize=False),
        ),
    ]
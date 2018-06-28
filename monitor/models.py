from django.db import models

class AlertSetting(models.Model):
    ENVTEMP = 'envtemp'
    ENVHUMIDITY = 'envhumidity'
    WATERTEMPFISHTANK = 'watertempfishtank'
    WATERTEMPSUMPTANK = 'watertempsumptank'
    WATERPH = 'waterph'
    ISFILLING = 'isfilling'
    WATERLEVELLOW = 'waterlevellow'
    WATERLEVELFULL = 'waterlevelfull'
    WATERFLOWFISHTANK = 'waterflowfishtank'
    WATERFLOWMAIN = 'waterflowmain'
    WATERFLOWVERTGROW = 'waterflowvertgrow'
    WATERFLOWHORIZGROW = 'waterflowhorizgrow'

    SENSOR_CHOICES = ((ENVTEMP, 'EnvTemp'), (ENVHUMIDITY, 'EnvHumidity'), (WATERTEMPFISHTANK, 'WaterTempFishTank'), (WATERTEMPSUMPTANK, 'WaterTempSumpTank'),
                        (WATERPH, 'WaterPH'), (ISFILLING, 'IsFilling'), (WATERLEVELLOW, 'WaterLevelLow'), (WATERLEVELFULL, 'WaterLevelFull'),
                        (WATERFLOWFISHTANK, 'WaterFlowFishTank'), (WATERFLOWMAIN, 'WaterFlowMain'), (WATERFLOWVERTGROW, 'WaterFlowVertGrow'), (WATERFLOWHORIZGROW, 'WaterFlowHorizGrow'))

    sensor = models.CharField(max_length=30, choices=SENSOR_CHOICES, default=ENVTEMP, primary_key=True)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    slider = models.CharField(max_length=100, default='<div>')
    label = models.CharField(max_length=30, default='label')
    order = models.IntegerField(default=1)

class WaterLevel(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)

class EnvHumidity(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class EnvTemp(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterLevelLow(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterLevelFull(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class IsFilling(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterFlowFishTank(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterFlowHorizGrow(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterFlowMain(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterFlowVertGrow(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterPH(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterTempFishTank(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class WaterTempSumpTank(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

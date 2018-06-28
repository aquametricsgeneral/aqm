from django.db import models

# Create your models here.

class EnvTemp(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Environmental Temperature Value"
        verbose_name_plural = "Environmental Temperature Values"

class WaterTempFishTank(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Fish Tank Water Temperature Value"
        verbose_name_plural = "Fish Tank Water Temperature Values"

class EnvHumidity(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Environmental Humidity Value"
        verbose_name_plural = "Environmental Humidity Values"

class WaterPH(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Water PH Value"
        verbose_name_plural = "Water PH Values"

class IsRain(models.Model):
    value = models.IntegerField()
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Rain Indicator Value"
        verbose_name_plural = "Rain Indicator Values"

class IsFilling(models.Model):
    value = models.IntegerField()
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Water Filling Indicator Value"
        verbose_name_plural = "Water Filling Indicator Values"

class WaterLevelLow(models.Model):
    value = models.IntegerField()
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Low Water Level Indicator Value"
        verbose_name_plural = "Low Water Level Indicator Values"

class WaterLevelFull(models.Model):
    value = models.IntegerField()
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Full Water Level Indicator Value"
        verbose_name_plural = "Full Water Level Indicator Values"

class WaterFlowFishTank(models.Model):
    value = models.IntegerField()
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Fish Tank Water Flow Indicator Value"
        verbose_name_plural = "Fish Tank Water Flow Indicator Values"

class WaterFlowMain(models.Model):
    value = models.IntegerField()
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Main Water Flow Indicator Value"
        verbose_name_plural = "Main Water Flow Indicator Values"

class WaterFlowVertGrow(models.Model):
    value = models.IntegerField()
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Vertical Growth Water Flow Indicator Value"
        verbose_name_plural = "Vertical Grow Water Flow Indicator Values"

class WaterFlowHorizGrow(models.Model):
    value = models.IntegerField()
    datetime = models.DateTimeField()
    class Meta:
        unique_together = ("value", "datetime")
        verbose_name = "Horizontal Growth Water Flow Indicator Value"
        verbose_name_plural = "Horizontal Growth Water Flow Indicator Values"
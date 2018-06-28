from django.contrib import admin
from monitor.models import EnvTemp, WaterTempFishTank, WaterTempSumpTank, EnvHumidity, WaterPH, IsFilling
from monitor.models import WaterFlowFishTank, WaterFlowMain, WaterFlowVertGrow, WaterFlowHorizGrow, WaterLevel
from monitor.models import AlertSetting
# Register your models here.

class MonitorAdmin(admin.ModelAdmin):
  date_hierarchy = 'datetime'
  search_fields = ['datetime']
  list_display = ('datetime','value','alert','lowerlimit','upperlimit','withinlimit')
  list_filter = ('datetime','value','alert','lowerlimit','upperlimit','withinlimit')

class WaterLevelAdmin(admin.ModelAdmin):
  date_hierarchy = 'datetime'
  search_fields = ['datetime']
  list_display = ('datetime','value')
  list_filter = ('datetime','value')

class AlertSettingAdmin(admin.ModelAdmin):
  list_display = ('sensor','label','alert','lowerlimit','upperlimit', 'slider','order')

admin.site.register(AlertSetting, AlertSettingAdmin)
admin.site.register(WaterLevel, WaterLevelAdmin)
admin.site.register(EnvTemp, MonitorAdmin)
admin.site.register(WaterTempFishTank, MonitorAdmin)
admin.site.register(EnvHumidity, MonitorAdmin)
admin.site.register(WaterPH, MonitorAdmin)
admin.site.register(WaterTempSumpTank, MonitorAdmin)
admin.site.register(IsFilling, MonitorAdmin)
admin.site.register(WaterFlowFishTank, MonitorAdmin)
admin.site.register(WaterFlowMain, MonitorAdmin)
admin.site.register(WaterFlowVertGrow, MonitorAdmin)
admin.site.register(WaterFlowHorizGrow, MonitorAdmin)

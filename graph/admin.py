from django.contrib import admin
from graph.models import EnvTemp, WaterTempFishTank, EnvHumidity, WaterPH, IsRain, WaterLevelLow, WaterLevelFull, IsFilling
from graph.models import WaterFlowFishTank, WaterFlowMain, WaterFlowVertGrow, WaterFlowHorizGrow
# Register your models here.

class MyAdmin(admin.ModelAdmin):
  date_hierarchy = 'datetime'
  search_fields = ['datetime']
  list_display = ('datetime','value')
  list_filter = ('datetime','value')

admin.site.register(EnvTemp, MyAdmin)
admin.site.register(WaterTempFishTank, MyAdmin)
admin.site.register(EnvHumidity, MyAdmin)
admin.site.register(WaterPH, MyAdmin)
admin.site.register(IsRain, MyAdmin)
admin.site.register(WaterLevelLow, MyAdmin)
admin.site.register(WaterLevelFull, MyAdmin)
admin.site.register(IsFilling, MyAdmin)
admin.site.register(WaterFlowFishTank, MyAdmin)
admin.site.register(WaterFlowMain, MyAdmin)
admin.site.register(WaterFlowVertGrow, MyAdmin)
admin.site.register(WaterFlowHorizGrow, MyAdmin)

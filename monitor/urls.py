from django.urls import path
from monitor import views

urlpatterns = [
    path('system_status/', views.system_status, name='system_status'),
    path('monitor_status/', views.monitor_status, name='monitor_status'),
    path('waterlevel_status/', views.waterlevel_status, name="waterlevel_status"),
    path('events/', views.events, name='events'),
    path('events_ajax/', views.events_ajax, name='events_ajax'),
    path('settings/', views.settings, name='settings'),
]

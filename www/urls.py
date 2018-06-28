from django.contrib import admin
from django.urls import path, include
from monitor import views as monitor_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', monitor_views.events, name='home'),
    path('graph/', include('graph.urls')),
    path('admin/', admin.site.urls),
    path('trend/', include('trend.urls')),
    path('journal/', include('journal.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('monitor/', include('monitor.urls')),
    path('chart/', include('chart.urls')),
    path('accounts/login/', auth_views.login, name='login'),
    path('accounts/logout/', auth_views.logout, {'next_page' : '/'}, name='logout'),
    ## Richard
    path('chat/', include('chat.urls')),
]

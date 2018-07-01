from django.contrib import admin
from django.urls import path, include, re_path
from monitor import views as monitor_views
from dashboard import views as dashboard_views
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
    re_path(r'profile/(?P<username>[a-zA-Z0-9]+)$', dashboard_views.get_user_profile, name='profile'),
    re_path(r'^accounts/password_reset/$', auth_views.password_reset, name='password_reset'),
    re_path(r'^accounts/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    re_path(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    re_path(r'^accounts/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    ## Richard
    path('chat/', include('chat.urls')),
]

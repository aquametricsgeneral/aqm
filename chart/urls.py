from django.urls import path, re_path
from chart import views

urlpatterns = [
    path('ajax_chart/', views.ajax_chart),
    re_path(r'^(?P<sensor>\w+)/$', views.chart, name="chart"),
]

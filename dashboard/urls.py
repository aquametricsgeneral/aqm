from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('ajax_data_for_gauge/', views.ajax_data_for_gauge),
]

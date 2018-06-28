from django.urls import path
from graph import views

urlpatterns = [
    path('', views.graph_integrated),
    path('db/', views.graph_db),
    path('db-ajax/', views.graph_db_ajax, name="graph-only"),
    path('gauge/', views.graph_gauge),
    path('integrated/', views.graph_integrated, name="graph-and-gauge"),
    path('ajax_data_for_gauge/', views.ajax_data_for_gauge),
    path('ajax_data_for_linechart/', views.ajax_data_for_linechart),
]

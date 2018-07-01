from django.shortcuts import render
from django.http import HttpResponse
import json
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from decimal import Decimal

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'dashboard/user_profile.html', {"user":user})

@login_required
def ajax_data_for_gauge(request):
    sensor_json={}
    sensor_id = None

    if request.method == 'GET':
        sensor_id = request.GET['sensor_id']

    sensor_model = apps.get_model("graph", sensor_id)
    sensor_query = sensor_model.objects.all().order_by('datetime').reverse()[:1].values('datetime','value')

    #for converting raw flow pulse data to liters per minute:
    #if sensor_id == 'WaterFlowMain':
    #    for i in range(0, len(sensor_query), 10):
    #        sensor_query[i]['value'] = round(sensor_query[i]['value'] * 2.22, 2)

    #if (sensor_id == 'WaterFlowFishTank' or sensor_id == 'WaterFlowVertGrow' or sensor_id == 'WaterFlowHorizGrow'):
    #    for i in range(0, len(sensor_query), 10):
    #        sensor_query[i]['value'] = round(sensor_query[i]['value'] * 0.13, 2)

    alertsetting_model = apps.get_model("monitor", 'AlertSetting')
    #convert the sensor_id to lowercase to match how it it set up in the AlertSetting model, required by Richard
    sensor_id_lowercase = sensor_id.lower()
    alertsetting_query = alertsetting_model.objects.filter(sensor=sensor_id_lowercase).values('lowerlimit','upperlimit')

    #for converting raw pulse data to liters per minutes for the green zones on the gauges:
    #if sensor_id_lowercase == 'waterflowmain':
    #    for i in range(0, len(alertsetting_query), 10):
    #        alertsetting_query[i]['lowerlimit'] = round(alertsetting_query[i]['lowerlimit'] * Decimal(2.22), 1)
    #        alertsetting_query[i]['upperlimit'] = round(alertsetting_query[i]['upperlimit'] * Decimal(2.22), 1)

    #if (sensor_id_lowercase == 'waterflowfishtank' or sensor_id_lowercase == 'waterflowvertgrow' or sensor_id_lowercase == 'waterflowhorizgrow'):
    #    for i in range(0, len(alertsetting_query), 10):
    #        alertsetting_query[i]['lowerlimit'] = round(alertsetting_query[i]['lowerlimit'] * Decimal(0.13), 1)
    #        alertsetting_query[i]['upperlimit'] = round(alertsetting_query[i]['upperlimit'] * Decimal(0.13), 1)

    status_msg = {'gauge_value': str(sensor_query[0]['value']), 'lowerlimit': str(alertsetting_query[0]['lowerlimit']), 'upperlimit': str(alertsetting_query[0]['upperlimit'])}

    sensor_json = json.dumps(status_msg)

    return HttpResponse(sensor_json)

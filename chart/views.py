import json
import pytz
from django.utils import timezone
from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def chart(request, sensor):
    a = {} #dict to construct json strings
    b = [] #list to store mutiple json strings
    sensor_json = {} #json to be passed to template
    sensor = sensor #sensor is passed from the URL string

    duration_int = 1

    start_datetime = datetime.now() - timedelta(hours=duration_int)
    end_datetime = datetime.now()
    timezone.activate(pytz.timezone("Asia/Singapore"))
    now = timezone.localtime(timezone.now())

    if (sensor == 'WaterLevel'):
        app = 'monitor'
    else:
        app = 'graph'

    sensor_model = apps.get_model(app, sensor)
    sensor_query = sensor_model.objects.filter(datetime__range=(start_datetime, end_datetime)).order_by('datetime').values('datetime','value')

    if sensor == 'WaterFlowMain':
        for i in range(0, len(sensor_query)):
            sensor_query[i]['value'] = round(sensor_query[i]['value'] * 2.22, 2)

    if (sensor == 'WaterFlowFishTank' or sensor == 'WaterFlowVertGrow' or sensor == 'WaterFlowHorizGrow'):
        for i in range(0, len(sensor_query)):
            sensor_query[i]['value'] = round(sensor_query[i]['value'] * 0.13, 2)

    for i in range(0, len(sensor_query)):
        a = {'x': timezone.localtime(sensor_query[i]['datetime']).isoformat(), 'y': str(sensor_query[i]['value'])}
        b.append(a)

    sensor_json['sensor_value'] = json.dumps(b)
    b.clear()

    duration_start = start_datetime.strftime("%I:%M %p, %d-%b-%y")
    duration_end = end_datetime.strftime("%I:%M %p, %d-%b-%y")
    duration_json = {'duration_start' : duration_start, 'duration_end' : duration_end}

    context_dict = {**duration_json, **sensor_json} #merge message_dict with sensor_json dict
    return render(request, 'chart/chart.html', context_dict)

@login_required
def ajax_chart(request):
    a = {}
    b = []
    sensor_json={}
    sensor = None
    duration_int = None

    if request.method == 'GET':
        sensor = request.GET['sensor_id']
        duration = request.GET['duration']

    duration_int = int(duration)

    start_datetime = datetime.now() - timedelta(hours=duration_int)
    end_datetime = datetime.now()
    timezone.activate(pytz.timezone("Asia/Singapore"))
    now = timezone.localtime(timezone.now())

    if (sensor == 'WaterLevel'):
        app = 'monitor'
    else:
        app = 'graph'

    sensor_model = apps.get_model(app, sensor)
    sensor_query = sensor_model.objects.filter(datetime__range=(start_datetime, end_datetime)).order_by('datetime').values('datetime','value')

    if sensor == 'WaterFlowMain':
        for i in range(0, len(sensor_query)):
            sensor_query[i]['value'] = round(sensor_query[i]['value'] * 2.22, 2)

    if (sensor == 'WaterFlowFishTank' or sensor == 'WaterFlowVertGrow' or sensor == 'WaterFlowHorizGrow'):
        for i in range(0, len(sensor_query)):
            sensor_query[i]['value'] = round(sensor_query[i]['value'] * 0.13, 2)

    for i in range(0, len(sensor_query)):
        a = {'x': timezone.localtime(sensor_query[i]['datetime']).isoformat(), 'y': str(sensor_query[i]['value'])}
        b.append(a)

    sensor_json = json.dumps(b)
    b.clear()

    return HttpResponse(sensor_json)

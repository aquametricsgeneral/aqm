from django.shortcuts import render
import json
import pytz
from django.utils import timezone
from django.apps import apps
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

def graph_gauge(request):

    return render(request, 'graph/graph_gauge.html')

def ajax_data_for_linechart(request):
    sensor_array = []
    sensor_json={}
    sensor_id = None

    if request.method == 'GET':
        sensor_id = request.GET['sensor_id']

    sensor_model = apps.get_model("graph", sensor_id)
    sensor_query = sensor_model.objects.all().order_by('datetime').reverse()[:1500]
    sensor_query = sensor_query.values('datetime','value')

    if sensor_id == 'IsRain':
        for i in range(0, len(sensor_query), 10):
            sensor_query[i]['value'] = round(sensor_query[i]['value'] / 100, 2)

    for i in range(0, len(sensor_query), 10):
        sensor_array.append([sensor_query[i]['datetime'].isoformat(), str(sensor_query[i]['value'])])

    sensor_json = json.dumps(sensor_array)

    return HttpResponse(sensor_json)

def ajax_data_for_gauge(request):
    sensor_array = []
    sensor_json={}
    sensor_id = None

    if request.method == 'GET':
        sensor_id = request.GET['sensor_id']

    if sensor_id == 'EnvTemp':
        sensor_label = 'Env Temp'

    if sensor_id == 'WaterTempFishTank':
        sensor_label = 'Water Temp'

    if sensor_id == 'EnvHumidity':
        sensor_label = 'Humidity'

    if sensor_id == 'WaterPH':
        sensor_label = 'Water pH'

    if sensor_id == 'IsRain':
        sensor_label = 'Rain'

    if sensor_id == 'WaterLevelLow':
        sensor_label = 'Water Low'

    if sensor_id == 'WaterLevelFull':
        sensor_label = 'Water Full'

    if sensor_id == 'IsFilling':
        sensor_label = 'Water Filling'

    if sensor_id == 'WaterFlowFishTank':
        sensor_label = 'Fish Tank Flow'

    if sensor_id == 'WaterFlowMain':
        sensor_label = 'Main Flow'

    if sensor_id == 'WaterFlowVertGrow':
        sensor_label = 'Vertical Flow'

    if sensor_id == 'WaterFlowHorizGrow':
        sensor_label = 'Horizontal Flow'

    sensor_model = apps.get_model("graph", sensor_id)
    sensor_query = sensor_model.objects.all().order_by('datetime').reverse()[:1]
    sensor_query = sensor_query.values('datetime','value')

    if sensor_id == 'IsRain':
        for i in range(0, len(sensor_query), 10):
            sensor_query[i]['value'] = round(sensor_query[i]['value'] / 100, 2)

    if sensor_id == 'WaterFlowMain':
        for i in range(0, len(sensor_query), 10):
            sensor_query[i]['value'] = round(sensor_query[i]['value'] * 2.22, 2)

    if (sensor_id == 'WaterFlowFishTank' or sensor_id == 'WaterFlowVertGrow' or sensor_id == 'WaterFlowHorizGrow'):
        for i in range(0, len(sensor_query), 10):
            sensor_query[i]['value'] = round(sensor_query[i]['value'] * 0.13, 2)

    sensor_array.append([sensor_label, str(sensor_query[0]['value'])])
    sensor_json = json.dumps(sensor_array)

    return HttpResponse(sensor_json)


def graph_all(request):

    #query for all the data points in the model
    EnvTemp_query = EnvTemp.objects.all().order_by('datetime').values('datetime','value')

    EnvTemp_list = [] #to pass this list to template

    for li in EnvTemp_query:
        EnvTemp_list.append([li['datetime'].isoformat(), str(li['value'])])

    timezone.activate(pytz.timezone("Asia/Singapore"))
    now = timezone.localtime(timezone.now())

    number_of_data_points = str(len(EnvTemp_list))

    message = number_of_data_points + " data points retrieved from database at " + now.strftime("%I:%M:%S %p") + " on " + now.strftime("%B %d, %Y") + " (Singapore time)."

    context_dict = {'message' : message,
                    'EnvTemp_list' : json.dumps(EnvTemp_list),
                    }
    return render(request, 'graph/graph_all.html', context_dict)

def graph_db(request):
    sensor_list = ["EnvTemp", "WaterTempFishTank", "EnvHumidity", "WaterPH", "IsRain",
                    "WaterLevelLow", "WaterLevelFull", "IsFilling",
                    "WaterFlowFishTank", "WaterFlowMain", "WaterFlowVertGrow", "WaterFlowHorizGrow"]
    sensor_array = []
    sensor_datapts = {}
    sensor_json={} #this dict holds the json dict to be passed to template
    sensor_slice = 1500
    sensor_skip = 10
    sensor_plotted = sensor_slice / sensor_skip

    for sensor_id in sensor_list:
        sensor_model = apps.get_model("graph", sensor_id)
        sensor_query = sensor_model.objects.all().order_by('datetime').reverse()[:sensor_slice]
        sensor_query = sensor_query.values('datetime','value')

        for i in range(0, len(sensor_query), sensor_skip):
            sensor_array.append([sensor_query[i]['datetime'].isoformat(), str(sensor_query[i]['value'])])


        sensor_json[sensor_id+"_value"] = json.dumps(sensor_array) #keys are suffixed with _value
        sensor_datapts[sensor_id+"_datapts"] = str(len(sensor_array))
        sensor_array.clear()

    timezone.activate(pytz.timezone("Asia/Singapore"))
    now = timezone.localtime(timezone.now())

    message = '%.0f' % sensor_plotted + " data points retrieved from database at " + now.strftime("%I:%M:%S %p") + " on " + now.strftime("%B %d, %Y") + " (Singapore time)."
    message_dict = {'message' : message}

    context_dict = {**message_dict, **sensor_json, **sensor_datapts} #merge message_dict with sensor_json dict

    return render(request, 'graph/graph_db.html', context_dict)

def graph_db_ajax(request):

    return render(request, 'graph/graph_db_ajax.html')

def graph_integrated(request):

    return render(request, 'graph/graph_integrated.html')

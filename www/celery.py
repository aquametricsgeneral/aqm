from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import datetime


app = Celery()


@periodic_task(run_every=(crontab(minute='*/2')), name="aquametrics_monitor_task", ignore_result=True)
def aquametrics_monitor_task():
    import os
    import sys
    import teleport
    from telegram.bot import Bot

    bot = Bot(token="600899467:AAHxAChF3L_CIlxo4H0JufRV2OWfjgRBhMc")
    channel = "-1001171180871"

    path = '/home/aquametrics/www'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE']='www.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    #lines above this are similar to wsgi, needed for standalone django script

    from django.core.mail import send_mail
    from django.apps import apps
    from django.utils import timezone, dateparse
    import pytz
    import time

    sensor_type = apps.get_model("monitor", "alertsetting")
    sensor = sensor_type.objects.all()
    sensor = list(sensor.values('sensor'))

    sensor = [i["sensor"] for i in sensor]

    for sensor_id in sensor:

        sensor_model = apps.get_model("monitor", sensor_id)
        timezone.activate(pytz.timezone("Asia/Singapore"))
        now = timezone.localtime(timezone.now())

#        print('Time now: ' + now.strftime("%I:%M:%S %p"))

        ### @@@ Check System STATUS @@@ ###
        #print("Checking Sensor Node Status...")
        sensor_query = sensor_model.objects.all().order_by('datetime').reverse()[:1]

        last_update_time = list(sensor_query.values('datetime'))

#        print("time last update: {} ".format(last_update_time[0]['datetime']))

        last_update_time = timezone.localtime(last_update_time[0]['datetime'])

        last_update_duration = int((now - last_update_time).total_seconds())
        
        node_status_path  ="/home/aquametrics/www/node.status"

        f = open(node_status_path,"r")
        status_in_file = f.readlines()
        f.close()

        status_in_file = status_in_file[0].split("\t")

        sys_status =status_in_file[0]
        down_up_time = dateparse.parse_datetime(status_in_file[1])
        notified_time = dateparse.parse_datetime(status_in_file[2])
        no_of_notification = int(status_in_file[3])

        last_notification_duration = int((now - notified_time).total_seconds())

#        print("last notification: {}".format(last_notification_duration))

        total_down_up_duration = int((now - down_up_time).total_seconds())


        if last_update_duration > 600 and sys_status == "1":

            no_of_notification = 0

            f = open(node_status_path,"w")
            f.write("0")
            f.write("\t")
            f.write(str(last_update_time))
            f.write("\t")
            f.write(str(now))
            f.write("\t")
            f.write(str(no_of_notification))
            f.close()

            msg="Sensor Node is OFFLINE! Warning: Alert Notification Will be Disabled"

            bot.sendMessage(chat_id=channel, text=msg)

            print("Node is offline")

        elif last_update_duration > 600 and sys_status == "0" and last_notification_duration > 7200:

            no_of_notification = no_of_notification + 1

            f = open(node_status_path,"w")
            f.write("0")
            f.write("\t")
            f.write(str(last_update_time))
            f.write("\t")
            f.write(str(now))
            f.write("\t")
            f.write(str(no_of_notification))
            f.close()

            msg="This is #{} Notification/s. Sensor Node is still offline since {} - {}sec. Warning: Alert Notification Is Still Disabled".format(str(no_of_notification),str(last_update_time),total_down_up_duration)

            bot.sendMessage(chat_id=channel, text=msg)

            print("This is #{} Notification/s. Node is still offline since {} - {}sec".format(str(no_of_notification),str(last_update_time),total_down_up_duration))
            
        elif last_update_duration <= 600 and sys_status == "0":
            
            no_of_notification = 0
            
            f = open(node_status_path,"w")
            f.write("1")
            f.write("\t")
            f.write(str(now))
            f.write("\t")
            f.write(str(now))
            f.write("\t")
            f.write(str(no_of_notification))    
            f.close()

            msg="Sensor Node is back ONLINE. Total down time is {}sec".format(total_down_up_duration)

            bot.sendMessage(chat_id=channel, text=msg)

            print('Node is back ONLINE.. total down time is {}sec'.format(total_down_up_duration))

        ### @@@ END - Check System STATUS @@@ ###
            
        ### @@@ Monitor Alert @@@ ###
        #print("Checking Alert Status...")
        alert_setting = list(sensor_query.values('alert'))

        if alert_setting[0]['alert'] == True and sys_status == "1":
            
            query_10 = sensor_model.objects.all().order_by('datetime').reverse()[:10]
            withinlimit = list(query_10.values('withinlimit'))
       
            counter = 0
            for i in withinlimit:
                if i['withinlimit'] == False:
                    counter = counter+1

                if counter == 10:
    
                    value = list(query_10.values('value'))

                    value = [i["value"] for i in value]

                    value_current= value[0]

                    value_max = max(value)

                    value_min = min(value)

                    value_ave = sum(value)/len(value)

                    upperlimit = list(sensor_query.values('upperlimit'))[0]['upperlimit']
                    
                    lowerlimit = list(sensor_query.values('lowerlimit'))[0]['lowerlimit']
                    
                    msg="Alarm!! {} is out of LIMIT [Current Limit:{} - {}]. Current: {}, Max: {}, Min: {}, Ave: {}".format(sensor_id,lowerlimit,upperlimit,value_current,value_max, value_min, value_ave)

                    bot.sendMessage(chat_id=channel, text=msg)

                    print("sending {} alarm".format(sensor_id))

      ### @@@ END - Monitor Alert @@@ ### 



##@shared_task
##def other_task():
##    f = open("/home/aquametrics/celery_other","a")
##    f.write(datetime.now().strftime("%d-%m %H:%M:%S"))
##    f.write("\t")
##    f.write("Hello World")
##    f.write("\n")
##    f.close()
##    print("{}  Hello World!".format(datetime.now().strftime("%d-%m %H:%M:%S")))
##
##@shared_task
##def some_task():
##    f = open("/home/aquametrics/celery_some","a")
##    f.write(datetime.now().strftime("%d-%m %H:%M:%S"))
##    f.write("\t")
##    f.write("Hello World")
##    f.write("\n")
##    f.close()
##    print("{}  Hello World!".format(datetime.now().strftime("%d-%m %H:%M:%S")))

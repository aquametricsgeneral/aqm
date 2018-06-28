from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import datetime

app = Celery()



##@periodic_task(run_every=(crontab(minute='*/1')), name="other_task", ignore_result=True)
##def other_task():
##    f = open("/home/aquametrics/celery_other","a")
##    f.write(datetime.now().strftime("%d-%m %H:%M:%S"))
##    f.write("\t")
##    f.write("Hello World")
##    f.write("\n")
##    f.close()
##    print("{}  Hello World!".format(datetime.now().strftime("%d-%m %H:%M:%S")))
##
##@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
##def some_task():
##    f = open("/home/aquametrics/celery_some","a")
##    f.write(datetime.now().strftime("%d-%m %H:%M:%S"))
##    f.write("\t")
##    f.write("Hello World")
##    f.write("\n")
##    f.close()
##    print("{}  Hello World!".format(datetime.now().strftime("%d-%m %H:%M:%S")))


        

##@periodic_task(run_every=(crontab(minute='*/1')), name="ph_task", ignore_result=True)
##def ph_task():
##    import os
##    import sys
##    import teleport
##
##    path = '/home/aquametrics/www'
##    if path not in sys.path:
##        sys.path.append(path)
##
##    os.environ['DJANGO_SETTINGS_MODULE']='www.settings'
##
##    from django.core.wsgi import get_wsgi_application
##    application = get_wsgi_application()
##
##    #lines above this are similar to wsgi, needed for standalone django script
##
##    from django.core.mail import send_mail
##    from django.apps import apps
##    from django.utils import timezone
##    import pytz
##    import time
##
##    def main():
##        alertPH('WaterPH', 6.0)
##
##    def alertPH(sensor_id, alert_value):
##
##        sensor_model = apps.get_model("graph", sensor_id)
##        alert_value = alert_value
##        timezone.activate(pytz.timezone("Asia/Singapore"))
##        now = timezone.localtime(timezone.now())
##
##        node_status_path  ="/home/aquametrics/www/ph.counter"
##    
##        f = open(node_status_path,"r")
##        counter = int(f.readlines()[0])
##        f.close()
##
##        print('Time now: ' + now.strftime("%I:%M:%S %p"))
##        print('Alert value: ' + str(alert_value))
##        print('Starting counter value: ' + str(counter))
##
##        if counter < 10:
##            sensor_query = sensor_model.objects.all().order_by('datetime').reverse()[:1]
##            sensor_query = sensor_query.values('value')
##            current_value = sensor_query[0]['value']
##
##            if current_value <= alert_value:
##                now = timezone.localtime(timezone.now())
##                counter += 1
##                print('current pH value: ' + str(current_value))
##                print('counter: ' + str(counter))
##                
##
##            else:
##                now = timezone.localtime(timezone.now())
##                counter = 0
##                print('current pH value: ' + str(current_value))
##                print('counter reset to: ' + str(counter))
##                
##            f = open(node_status_path,"w")
##            f.write(str(counter))
##            f.close()
##            
##        else:
##
##            if counter == 10:
##
##                counter +=1
##                
##                print('Sending email alert...')
##                send_mail(
##                    'LOW WATER PH ALERT',
##                    'Water pH value is lower than ' + str(alert_value) + ' for more than 10 minutes.',
##                    'aquametricsgeneral@gmail.com',
##                    ['tengthuan@gmail.com', 'hongjin86@gmail.com'],
##                    fail_silently=False,
##                    )
##                print('Email alert sent. Going to sleep for 1 hour before checking the pH again.')
##
##                
##
##            elif counter > 10 and counter < 60:
##                counter +=1
##
##            else:
##                counter = 0
##
##            f = open(node_status_path,"w")
##            f.write(str(counter))
##            f.close()         
##
##
##    main()


def retrive_limit(sensor_id):

    import pytz
    import time
    import os
    import sys
    import teleport
    
    path = '/home/aquametrics/www'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE']='www.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    from django.apps import apps
    from django.utils import timezone

    threshold_db = apps.get_model("graph", sensor_id)

    
    threshold = threshold_db.objects.values('sensor')

    print(listthreshold)
    



@periodic_task(run_every=(crontab(minute='*/2')), name="temp_task", ignore_result=True)
def temp_task():
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
    from django.utils import timezone
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

        print('Time now: ' + now.strftime("%I:%M:%S %p"))

        sensor_query = sensor_model.objects.all().order_by('datetime').reverse()[:1]
        alert_setting = list(sensor_query.values('alert'))

        if alert_setting[0]['alert'] == True:
            
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

                
            
##                print('Sending email alert...')
##                send_mail(
##                    'LOW WATER PH ALERT',
##                    'Water pH value is lower than ' + str(alert_value) + ' for more than 10 minutes.',
##                    'aquametricsgeneral@gmail.com',
##                    ['tengthuan@gmail.com', 'hongjin86@gmail.com'],
##                    fail_silently=False,
##                    )
##                print('Email alert sent. Going to sleep for 1 hour before checking the pH again.')


        



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

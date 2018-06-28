from django.shortcuts import render
from django.http import HttpResponse
from bokeh.layouts import Row, Column
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models.tools import HoverTool, WheelZoomTool, PanTool, ResetTool, BoxZoomTool, SaveTool, UndoTool, RedoTool, CrosshairTool
from bokeh.models import ColumnDataSource, CustomJS, FuncTickFormatter, Legend
from bokeh.models.widgets import RangeSlider, DateRangeSlider, DatePicker, Div, Panel, Tabs
import pandas as pd
from django.apps import apps
from datetime import date, datetime
from bokeh.models import Range1d, DatetimeAxis, LinearAxis
import pytz
import json
from bokeh.models import Line, Circle
#from math import pi

def envtemp(request):
    return render(request, 'trend/envtemp.html')

def watertemp(request):
    return render(request, 'trend/watertemp.html')

def humidity(request):
    return render(request, 'trend/humidity.html')

def waterph(request):
    return render(request, 'trend/waterph.html')

def isfilling(request):
    return render(request, 'trend/isfilling.html')

def overlay(request):
    return render(request, 'trend/overlay.html')

def ajax_overlay(request):

    if request.method == 'GET':
        sensor_id = request.GET['sensor_id']

    if sensor_id == 'EnvTemp':
        sensor_label = 'Environment Temperature [°C]'
        sensor_y_range = (20, 40)
        graph1_color = 'red'
        graph2_color = 'gold'
        slider_start = 0
        slider_end = 50

    if sensor_id == 'WaterTempFishTank':
        sensor_label = 'Fish Tank Water Temperature [°C]'
        sensor_y_range = (20, 40)
        graph1_color = 'green'
        graph2_color = 'deeppink'
        slider_start = 0
        slider_end = 50

    if sensor_id == 'EnvHumidity':
        sensor_label = 'Humidity [%]'
        sensor_y_range = (30, 100)
        graph1_color = 'orange'
        graph2_color = 'navy'
        slider_start = 30
        slider_end = 100

    if sensor_id == 'WaterPH':
        sensor_label = 'Water pH'
        sensor_y_range = (4, 8)
        graph1_color = 'blue'
        graph2_color = 'indigo'
        slider_start = 0
        slider_end = 14

    if sensor_id == 'IsFilling':
        sensor_label = 'IsFilling'
        sensor_y_range = (0, 1)
        graph1_color = 'pink'
        graph2_color = 'green'
        slider_start = -1
        slider_end = 2

    if sensor_id == 'WaterLevelLow':
        sensor_label = 'WaterLevelLow'
        sensor_y_range = (0, 1)
        graph1_color = 'gray'
        graph2_color = 'green'
        slider_start = -1
        slider_end = 2

    if sensor_id == 'WaterLevelFull':
        sensor_label = 'WaterLevelFull'
        sensor_y_range = (0, 1)
        graph1_color = 'purple'
        graph2_color = 'green'
        slider_start = -1
        slider_end = 2

    if sensor_id == 'WaterFlowFishTank':
        sensor_label = 'WaterFlowFishTank'
        sensor_y_range = (0, 12)
        graph1_color = 'crimson'
        graph2_color = 'green'
        slider_start = 0
        slider_end = 100

    if sensor_id == 'WaterFlowMain':
        sensor_label = 'WaterFlowMain'
        sensor_y_range = (0, 12)
        graph1_color = 'orange'
        graph2_color = 'green'
        slider_start = 0
        slider_end = 100

    if sensor_id == 'WaterFlowVertGrow':
        sensor_label = 'WaterFlowVertGrow'
        sensor_y_range = (0, 12)
        graph1_color = 'indigo'
        graph2_color = 'green'
        slider_start = 0
        slider_end = 100

    if sensor_id == 'WaterFlowHorizGrow':
        sensor_label = 'WaterFlowHorizGrow'
        sensor_y_range = (0, 12)
        graph1_color = 'navy'
        graph2_color = 'green'
        slider_start = 0
        slider_end = 100

    sensor_model = apps.get_model("graph", sensor_id)
    sensor_query = sensor_model.objects.all().order_by('datetime').reverse()
    sensor_query = sensor_query.values('datetime','value')

    #extract the values inside the queryset and place into the temp dict
    sensor_dict = {'datetimes':[], 'values':[]}

    for j in range(len(sensor_query)):
        sensor_dict['datetimes'].append(sensor_query[j]['datetime'])
        sensor_dict['values'].append(sensor_query[j]['value'])

    #create a pandas dataframe using the temp dict, name the columns, convert the timezone
    df = pd.DataFrame(data=sensor_dict, columns=['datetimes','values'])
    df.datetimes = pd.DatetimeIndex(pd.to_datetime(df.datetimes)).tz_convert(pytz.timezone('Asia/Singapore'))
    df.datetimes.tolist()

    #create a bokeh columndatasource
    source = ColumnDataSource(data=dict(datetimes=df['datetimes'], values=df['values']))

    source.add(df['datetimes'].apply(lambda d: d.strftime('%Y-%m-%d, %H:%M:%S')), 'datetimes_formatted')

    # query for data from the model in the Journal app
    journal_model = apps.get_model("journal", "Post")
    journal_query = journal_model.objects.all().order_by('published_date').reverse()
    journal_query = journal_query.values('published_date','title', 'text', 'value')

    #extract the values inside the queryset and place into a temporary journal_dict
    journal_dict = {'published_date':[], 'title':[], 'text':[], 'value':[]}

    for j in range(len(journal_query)):
        journal_dict['published_date'].append(journal_query[j]['published_date'])
        journal_dict['title'].append(journal_query[j]['title'])
        journal_dict['text'].append(journal_query[j]['text'])
        journal_dict['value'].append(journal_query[j]['value'])

    #create a pandas dataframe using the temporary journal_dict, name the columns, convert the timezone
    df2 = pd.DataFrame(data=journal_dict, columns=['published_date','title','text', 'value'])
    df2.published_date = pd.DatetimeIndex(pd.to_datetime(df2.published_date)).tz_convert(pytz.timezone('Asia/Singapore'))
    df2.published_date.tolist()

    #create a bokeh columndatasource for data in the Journal app
    source2 = ColumnDataSource(data=dict(published_date=df2['published_date'], title=df2['title'], text=df2['text'], value=df2['value']))

    #add a column in the columndatasource with formatted datetime
    source2.add(df2['published_date'].apply(lambda d: d.strftime('%Y-%m-%d, %H:%M:%S')), 'published_date_formatted')

    # create a new plot with a datetime axis type
    p1 = figure(plot_width=1200, plot_height=500, x_axis_type="datetime", y_range=sensor_y_range,
                x_range=Range1d(start=datetime.fromtimestamp(1513094400), end=datetime.now(tz=pytz.timezone('Asia/Singapore'))),
                tools=[WheelZoomTool(), PanTool(), ResetTool(), BoxZoomTool(), SaveTool(), UndoTool(), RedoTool(), CrosshairTool()],
                title="All data for " + sensor_id)

    # set x-axis label
    p1.xaxis.axis_label = 'Date & Time for 1st Graph'

    # set y-axis label
    p1.yaxis.axis_label = sensor_label

    # create 2nd datetime x-axis so that graphs can be separated
    p1.extra_x_ranges = {"datetime_axis_2": Range1d(start=datetime.fromtimestamp(1513094400), end=datetime.now(tz=pytz.timezone('Asia/Singapore')))}

    p1.extra_y_ranges = {"journal_axis": Range1d(start=-100, end=100)}

    # add 2nd datetime x-axis to the plot
    p1.add_layout(DatetimeAxis(x_range_name="datetime_axis_2", axis_label='Date & Time for 2nd Graph'), 'below')
    p1.add_layout(LinearAxis(y_range_name="journal_axis", axis_label='journal'), 'right')

    # create a Line glyph for 1st set of sensor data
    g1 = Line(x='datetimes', y='values', line_color=graph1_color, line_alpha=1)
    # create a duplicate Line glyph to be used in overlay comparison
    g2 = Line(x='datetimes', y='values', line_color=graph2_color, line_alpha=1)
    # create a Circle glyph plotting the entries from the Journal app
    g3 = Circle(x='published_date', y='value', fill_color='black', fill_alpha=1)

    # create the respective renderers
    g1_r = p1.add_glyph(source_or_glyph=source, glyph=g1)
    g2_r = p1.add_glyph(source_or_glyph=source, glyph=g2, x_range_name="datetime_axis_2")
    g3_r = p1.add_glyph(source_or_glyph=source2, glyph=g3, y_range_name="journal_axis")

    # create a hover tool for g1 and g2 glyphs
    g1g2_hover = HoverTool(renderers=[g1_r,g2_r],
            tooltips=[
                ('value', '@values{0.00}'),
                ('date', '@datetimes_formatted'),
            ]
        )

    # create a hover tool for g3 glyph
    g3_hover = HoverTool(renderers=[g3_r],
            tooltips=[
                ('published_date', '@published_date_formatted'),
                ('title', '@title'),
                ('text', '@text'),
                ('journal value', '@value'),
            ]
        )

    # add the hover tools to the plot
    p1.add_tools(g1g2_hover)
    p1.add_tools(g3_hover)

    #create interactive legends
    legend = Legend(items=[
    (sensor_id + " 1"   , [g1_r]),
    (sensor_id + " 2"   , [g2_r]),
    ("Journal"          , [g3_r]),
    ], location=(0, 0), click_policy='hide')

    # define legend label string variables to be used by widgets
    legend_label_1 = legend.items[0].label['value']
    legend_label_2 = legend.items[1].label['value']

    # add legend to plots
    p1.add_layout(legend, 'right')

    #Javascript code to format the datetime x-axis to localize the datetimes manually using this workaround
    datetime_formatter="""
        //var sg_date = new Date(tick).toLocaleString("en-US", {timeZone: "Asia/Singapore"})
        var timestring = tick;
        var locale_date = new Date(timestring).toLocaleDateString();
        var locale_time = new Date(timestring).toLocaleTimeString();
        var locale_datetime = locale_date + " " + locale_time;
        return locale_datetime
    """
    p1.xaxis.formatter = FuncTickFormatter(code=datetime_formatter)

    #create a y-axis range slider for better visibility during analysis
    jscode1="""
        //cb_obj.value refers to the rangeslider's value, which is a tuple containing 2 values, assign this to y_range
        var y_range = cb_obj.value;

        //first item of y_range is the min value, second item is the max value
        var y_min = y_range[0];
        var y_max = y_range[1];

        //update the start and end of the plot's range
        plot.y_range.start = y_min;
        plot.y_range.end = y_max;
        plot.change.emit();
    """

    jscode2="""
        //cb_obj.value refers to the rangeslider's value, which is a tuple containing 2 values, assign this to y_range
        var y_range = cb_obj.value;

        //first item of y_range is the min value, second item is the max value
        var y_min = y_range[0];
        var y_max = y_range[1];

        //update the plot's extra_y_ranges, the variables are passed in when calling out RangeSlider
        plot.extra_y_ranges['%s'].start = y_min;
        plot.extra_y_ranges['%s'].end = y_max;
        plot.change.emit();
    """

    div_1 = Div(text="""Range start date: """, width=800, height=5)
    div_2 = Div(text="""Range end date: """, width=800, height=5)
    div_2A = Div(text="""No. of days: """, width=800, height=5)
    div_3 = Div(text="""Range start date: """, width=800, height=5)
    div_4 = Div(text="""Range end date: """, width=800, height=5)
    div_4A = Div(text="""No. of days: """, width=800, height=5)
    div_5 = Div(text="""Calendar start date: """, width=800, height=5)
    div_6 = Div(text="""Calendar end date: """, width=800, height=5)
    div_7 = Div(text="""Calendar start date: """, width=800, height=5)
    div_8 = Div(text="""Calendar end date: """, width=800, height=5)

    div_A = Div(text="""%s""" % legend_label_1, width=800, height=5)
    div_B = Div(text="""%s""" % legend_label_2, width=800, height=5)
    div_C = Div(text="""%s""" % legend_label_1, width=800, height=5)
    div_D = Div(text="""%s""" % legend_label_2, width=800, height=5)

    # Javascript callback1 for adjusting the datetime x-axis according to the date range slider drs1
    callback1 = """
        // cb_obj refers to the date range slider, which has attribute "value" in the form of tuple
        var dateslider_range = cb_obj.value;

        // extract the start and end datetime from the tuple
        var dateslider_start = dateslider_range[0];
        var dateslider_end = dateslider_range[1];

        var js_start = new Date(dateslider_start);
        var js_end = new Date(dateslider_end);

        js_start.setHours(0,0,0);
        js_end.setHours(23,59,59);

        var one_day=1000*60*60*24;
        var diff_ms = Math.abs(js_end - js_start);
        var diff_day = Math.round(diff_ms/one_day);

        div_1.text = "Range start date: " + js_start.toString() ;
        div_2.text = "Range end date: " + js_end.toString();
        div_2A.text = "No. of days: " + diff_day;

        var posix_start = js_start.getTime();
        var posix_end = js_end.getTime();

        // update the x-axis range
        plot.x_range.start = posix_start;
        plot.x_range.end = posix_end;

        plot.change.emit();
    """

    # Javascript callback2 for adjusting the 2nd datetime x-axis according to the date range slider drs2
    callback2 = """
        // cb_obj refers to the date range slider, which has attribute "value" in the form of tuple
        var dateslider_range = cb_obj.value;

        // extract the start and end datetime from the tuple
        var dateslider_start = dateslider_range[0];
        var dateslider_end = dateslider_range[1];

        var js_start = new Date(dateslider_start);
        var js_end = new Date(dateslider_end);

        js_start.setHours(0,0,0);
        js_end.setHours(23,59,59);

        var one_day=1000*60*60*24;
        var diff_ms = Math.abs(js_end - js_start);
        var diff_day = Math.round(diff_ms/one_day);

        div_3.text = "Range start date: " + js_start.toString();
        div_4.text = "Range end date: " + js_end.toString();
        div_4A.text = "No. of days: " + diff_day;

        var posix_start = js_start.getTime();
        var posix_end = js_end.getTime();

        // update the x-axis range
        plot.extra_x_ranges['datetime_axis_2'].start = posix_start;
        plot.extra_x_ranges['datetime_axis_2'].end = posix_end;

        plot.change.emit();
    """

    # Javascript callback3 for adjusting the datetime x-axis according to the calendar date picker dp1
    callback3 = """
        var datepicker_date = cb_obj.value;

        var start_date = new Date(datepicker_date);
        start_date.setHours(0,0,0);

        var end_date = new Date();
        end_date.setTime(start_date.getTime());
        end_date.setDate(start_date.getDate()+1);

        div_5.text = "Calendar start date: " + start_date.toString() ;
        div_6.text = "Calendar end date: " + end_date.toString();

        var posix_start = start_date.getTime();
        var posix_end = end_date.getTime();

        plot.x_range.start = posix_start;
        plot.x_range.end = posix_end;

        plot.change.emit();
    """

    # Javascript callback4 for adjusting the 2nd datetime x-axis according to the calendar date picker dp2
    callback4 = """
        var datepicker_date = cb_obj.value;

        var start_date = new Date(datepicker_date);
        start_date.setHours(0,0,0);

        var end_date = new Date();
        end_date.setTime(start_date.getTime());
        end_date.setDate(start_date.getDate()+1);

        div_7.text = "Calendar start date: " + start_date.toString() ;
        div_8.text = "Calendar end date: " + end_date.toString();

        var posix_start = start_date.getTime();
        var posix_end = end_date.getTime();

        plot.extra_x_ranges['datetime_axis_2'].start = posix_start;
        plot.extra_x_ranges['datetime_axis_2'].end = posix_end;

        plot.change.emit();
    """

    # range slider for adjusting the EnvTemp y-axis
    rs1 = RangeSlider(start=slider_start, end=slider_end, value=sensor_y_range, step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color=graph1_color, direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode1))

    rs2 = RangeSlider(start=-100, end=100, value=(0,10), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color="black", direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode2 % ('journal_axis','journal_axis')))

    # date range sliders for period to period data comparison
    drs1 = DateRangeSlider(start=date.fromtimestamp(1513094400), end=date.today(), value=(date.fromtimestamp(1513094400), date.today()), step=1, format='%d %b %Y',
                    height=5, width=650, show_value=False, callback=CustomJS(args=dict(plot=p1, div_1=div_1, div_2=div_2, div_2A=div_2A), code=callback1 ))

    drs2 = DateRangeSlider(start=date.fromtimestamp(1513094400), end=date.today(), value=(date.fromtimestamp(1513094400), date.today()), step=1, format='%d %b %Y',
                    height=5, width=650, show_value=False, callback=CustomJS(args=dict(plot=p1, div_3=div_3, div_4=div_4, div_4A=div_4A), code=callback2 ))

    # calendar date pickers for 1-day to 1-day data omparison
    dp1 = DatePicker(value=date.today(), callback=CustomJS(args=dict(plot=p1, div_5=div_5, div_6=div_6), code=callback3 ))

    dp2 = DatePicker(value=date.today(), callback=CustomJS(args=dict(plot=p1, div_7=div_7, div_8=div_8), code=callback4 ))

    # create tabs for slider / calender selection methods
    tab_slider = Panel(child=Column(children=[
                        Row(children=[Column(children=[div_A,div_1,div_2,div_2A,drs1]),Column(children=[div_B,div_3,div_4,div_4A,drs2])]),
                        ]), title="slider")

    tab_calendar = Panel(child=Column(children=[
                            Row(children=[Column(children=[div_C,div_5,div_6,dp1]),Column(children=[div_D,div_7,div_8,dp2])]),
                            ]), title="calendar")

    tabs_picker = Tabs(tabs=[ tab_slider, tab_calendar ])

    plots = Column(children=[
                            Row(children=[rs1,p1,rs2]),
                            tabs_picker,
                            ])

    #Store components
    script, div = components(plots)

    script_dict = {'script' : script}
    div_dict = {'div' : div}
    bokeh_dict = {**script_dict, **div_dict} #merge dicts
    bokeh_json = json.dumps(bokeh_dict)

    #Feed them to the Django template.
    return HttpResponse(bokeh_json)

def all_trend_lines(request):
    sensor_list = ["EnvTemp", "WaterTempFishTank", "EnvHumidity", "WaterPH"]
    dfs = [] #list for storing panda dataframe
    sources = [] #list for storing Bokeh columndatasource

    for i in range(len(sensor_list)):
        #query for models in database
        sensor_model = apps.get_model("graph", sensor_list[i])
        sensor_query = sensor_model.objects.all().order_by('datetime').reverse()
        sensor_query = sensor_query.values('datetime','value')

        #extract the values inside the queryset and place into the temp dict
        sensor_dict = {'datetimes':[], 'values':[]}

        for j in range(len(sensor_query)):
            sensor_dict['datetimes'].append(sensor_query[j]['datetime'])
            sensor_dict['values'].append(sensor_query[j]['value'])

        #create a pandas dataframe using the temp dict, name the columns, convert the timezone
        df = pd.DataFrame(data=sensor_dict, columns=['datetimes','values'])
        dfs.append(df)
        dfs[i].datetimes = pd.DatetimeIndex(pd.to_datetime(dfs[i].datetimes)).tz_convert(pytz.timezone('Asia/Singapore'))
        dfs[i].datetimes.tolist()

        #create a bokeh columndatasource
        source = ColumnDataSource(data=dict(datetimes=dfs[i]['datetimes'], values=dfs[i]['values']))
        sources.append(source)
        sources[i].add(dfs[i]['datetimes'].apply(lambda d: d.strftime('%Y-%m-%d, %H:%M:%S')), 'datetimes_formatted')

    # query for data from the model in the Journal app
    journal_model = apps.get_model("journal", "Post")
    journal_query = journal_model.objects.all().order_by('published_date').reverse()
    journal_query = journal_query.values('published_date','title', 'text', 'value')

    #extract the values inside the queryset and place into a temporary journal_dict
    journal_dict = {'published_date':[], 'title':[], 'text':[], 'value':[]}

    for j in range(len(journal_query)):
        journal_dict['published_date'].append(journal_query[j]['published_date'])
        journal_dict['title'].append(journal_query[j]['title'])
        journal_dict['text'].append(journal_query[j]['text'])
        journal_dict['value'].append(journal_query[j]['value'])

    #create a pandas dataframe using the temporary journal_dict, name the columns, convert the timezone
    df2 = pd.DataFrame(data=journal_dict, columns=['published_date','title','text', 'value'])
    df2.published_date = pd.DatetimeIndex(pd.to_datetime(df2.published_date)).tz_convert(pytz.timezone('Asia/Singapore'))
    df2.published_date.tolist()

    #create a bokeh columndatasource for data in the Journal app
    source2 = ColumnDataSource(data=dict(published_date=df2['published_date'], title=df2['title'], text=df2['text'], value=df2['value']))

    #add a column in the columndatasource with formatted datetime
    source2.add(df2['published_date'].apply(lambda d: d.strftime('%Y-%m-%d, %H:%M:%S')), 'published_date_formatted')

    # create a new plot with a datetime axis type
    p1 = figure(plot_width=1200, plot_height=500, x_axis_type="datetime", y_range=(20,40),
                x_range=Range1d(start=datetime.fromtimestamp(1513094400), end=datetime.now(tz=pytz.timezone('Asia/Singapore'))),
                tools=[WheelZoomTool(), PanTool(), ResetTool(), BoxZoomTool(), SaveTool(), UndoTool(), RedoTool(), CrosshairTool()],
                title="All data for " + sensor_list[0])

    # set x-axis label
    p1.xaxis.axis_label = 'Date & Time for 1st Graph'

    # set y-axis label
    p1.yaxis.axis_label = 'Environment Temperature [°C]'

    # set extra y-axes label and range
    p1.extra_y_ranges = {"humidity_axis": Range1d(start=30, end=100), "waterph_axis": Range1d(start=4, end=8),
                         "watertemp_axis": Range1d(start=20, end=40), "journal_axis": Range1d(start=-100, end=100)}

    # create 2nd datetime x-axis so that graphs can be separated
    p1.extra_x_ranges = {"datetime_axis_2": Range1d(start=datetime.fromtimestamp(1513094400), end=datetime.now(tz=pytz.timezone('Asia/Singapore')))}

    # add 2nd y-axis to the plot.
    p1.add_layout(LinearAxis(y_range_name="humidity_axis", axis_label='Humidity [%]'), 'right')
    p1.add_layout(LinearAxis(y_range_name="waterph_axis", axis_label='Water pH'), 'right')
    p1.add_layout(LinearAxis(y_range_name="watertemp_axis", axis_label='Fish Tank Water Temperature [°C]'), 'left')
    p1.add_layout(LinearAxis(y_range_name="journal_axis", axis_label='Journal'), 'left')

    # add 2nd datetime x-axis to the plot
    p1.add_layout(DatetimeAxis(x_range_name="datetime_axis_2", axis_label='Date & Time for 2nd Graph'), 'below')

    # glyph for EnvTemp 1st graph
    g1 = Line(x='datetimes', y='values', line_color='red', line_alpha=1)
    # glyph for EnvTemp 2nd graph
    g2 = Line(x='datetimes', y='values', line_color='gold', line_alpha=1)
    # glyph for WaterTemp 1st graph
    g3 = Line(x='datetimes', y='values', line_color='green', line_alpha=1)
    # glyph for WaterTemp 2nd graph
    g4 = Line(x='datetimes', y='values', line_color='deeppink', line_alpha=1)
    # glyph for humidity 1st graph
    g5 = Line(x='datetimes', y='values', line_color='orange', line_alpha=1)
    # glyph for humidity 2nd graph
    g6 = Line(x='datetimes', y='values', line_color='navy', line_alpha=1)
    # glyph for water pH 1st graph
    g7 = Line(x='datetimes', y='values', line_color='blue', line_alpha=1)
    # glyph for water pH 2nd graph
    g8 = Line(x='datetimes', y='values', line_color='indigo', line_alpha=1)
    # glyph for Journal entries
    g11 = Circle(x='published_date', y='value', fill_color='black', fill_alpha=1)

    # create the respective renderers
    g1_r = p1.add_glyph(source_or_glyph=sources[0], glyph=g1)
    g2_r = p1.add_glyph(source_or_glyph=sources[0], glyph=g2, x_range_name="datetime_axis_2")
    g3_r = p1.add_glyph(source_or_glyph=sources[1], glyph=g3, y_range_name="watertemp_axis")
    g4_r = p1.add_glyph(source_or_glyph=sources[1], glyph=g4, y_range_name="watertemp_axis", x_range_name="datetime_axis_2")
    g5_r = p1.add_glyph(source_or_glyph=sources[2], glyph=g5, y_range_name="humidity_axis")
    g6_r = p1.add_glyph(source_or_glyph=sources[2], glyph=g6, y_range_name="humidity_axis", x_range_name="datetime_axis_2")
    g7_r = p1.add_glyph(source_or_glyph=sources[3], glyph=g7, y_range_name="waterph_axis")
    g8_r = p1.add_glyph(source_or_glyph=sources[3], glyph=g8, y_range_name="waterph_axis", x_range_name="datetime_axis_2")
    g11_r = p1.add_glyph(source_or_glyph=source2, glyph=g11, y_range_name="journal_axis")

    # create a hover tool for all line glyphs
    gall_hover = HoverTool(renderers=[g1_r,g2_r,g3_r,g4_r,g5_r,g6_r,g7_r,g8_r],
            tooltips=[
                ('value', '@values{0.00}'),
                ('date', '@datetimes_formatted'),
            ]
        )

    # create a hover tool for circle glyph
    g11_hover = HoverTool(renderers=[g11_r],
            tooltips=[
                ('published_date', '@published_date_formatted'),
                ('title', '@title'),
                ('text', '@text'),
                ('journal value', '@value'),
            ]
        )

    # add the hover tools to the plot
    p1.add_tools(gall_hover)
    p1.add_tools(g11_hover)

    #create interactive legends
    legend = Legend(items=[
    ("EnvTemp 1", [g1_r]),
    ("EnvTemp 2", [g2_r]),
    ("WaterTemp 1", [g3_r]),
    ("WaterTemp 2", [g4_r]),
    ("Humidity 1", [g5_r]),
    ("Humidity 2", [g6_r]),
    ("pH 1", [g7_r]),
    ("pH 2", [g8_r]),
    ("Journal", [g11_r]),
    ], location=(0, 0), click_policy='hide')

    # add legend to plots
    p1.add_layout(legend, 'right')

    #Javascript code to format the datetime x-axis to localize the datetimes manually using this workaround
    datetime_formatter="""
        //var sg_date = new Date(tick).toLocaleString("en-US", {timeZone: "Asia/Singapore"})
        var timestring = tick;
        var locale_date = new Date(timestring).toLocaleDateString();
        var locale_time = new Date(timestring).toLocaleTimeString();
        var locale_datetime = locale_date + " " + locale_time;
        return locale_datetime
    """
    p1.xaxis.formatter = FuncTickFormatter(code=datetime_formatter)

    #create a y-axis range slider for better visibility during analysis
    jscode1="""
        //cb_obj.value refers to the rangeslider's value, which is a tuple containing 2 values, assign this to y_range
        var y_range = cb_obj.value;

        //first item of y_range is the min value, second item is the max value
        var y_min = y_range[0];
        var y_max = y_range[1];

        //update the start and end of the plot's range
        plot.y_range.start = y_min;
        plot.y_range.end = y_max;
        plot.change.emit();
    """

    jscode2="""
        //cb_obj.value refers to the rangeslider's value, which is a tuple containing 2 values, assign this to y_range
        var y_range = cb_obj.value;

        //first item of y_range is the min value, second item is the max value
        var y_min = y_range[0];
        var y_max = y_range[1];

        //update the plot's extra_y_ranges, the variables are passed in when calling out RangeSlider
        plot.extra_y_ranges['%s'].start = y_min;
        plot.extra_y_ranges['%s'].end = y_max;
        plot.change.emit();
    """

    div_1 = Div(text="""Range start date: """, width=800, height=5)
    div_2 = Div(text="""Range end date: """, width=800, height=5)
    div_2A = Div(text="""No. of days: """, width=800, height=5)
    div_3 = Div(text="""Range start date: """, width=800, height=5)
    div_4 = Div(text="""Range end date: """, width=800, height=5)
    div_4A = Div(text="""No. of days: """, width=800, height=5)
    div_5 = Div(text="""Calendar start date: """, width=800, height=5)
    div_6 = Div(text="""Calendar end date: """, width=800, height=5)
    div_7 = Div(text="""Calendar start date: """, width=800, height=5)
    div_8 = Div(text="""Calendar end date: """, width=800, height=5)

    div_A = Div(text="""Graph 1""", width=800, height=5)
    div_B = Div(text="""Graph 2""", width=800, height=5)
    div_C = Div(text="""Graph 1""", width=800, height=5)
    div_D = Div(text="""Graph 2""", width=800, height=5)

    # Javascript callback1 for adjusting the datetime x-axis according to the date range slider drs1
    callback1 = """
        // cb_obj refers to the date range slider, which has attribute "value" in the form of tuple
        var dateslider_range = cb_obj.value;

        // extract the start and end datetime from the tuple
        var dateslider_start = dateslider_range[0];
        var dateslider_end = dateslider_range[1];

        var js_start = new Date(dateslider_start);
        var js_end = new Date(dateslider_end);

        js_start.setHours(0,0,0);
        js_end.setHours(23,59,59);

        var one_day=1000*60*60*24;
        var diff_ms = Math.abs(js_end - js_start);
        var diff_day = Math.round(diff_ms/one_day);

        div_1.text = "Range start date: " + js_start.toString() ;
        div_2.text = "Range end date: " + js_end.toString();
        div_2A.text = "No. of days: " + diff_day;

        var posix_start = js_start.getTime();
        var posix_end = js_end.getTime();

        // update the x-axis range
        plot.x_range.start = posix_start;
        plot.x_range.end = posix_end;

        plot.change.emit();
    """

    # Javascript callback2 for adjusting the 2nd datetime x-axis according to the date range slider drs2
    callback2 = """
        // cb_obj refers to the date range slider, which has attribute "value" in the form of tuple
        var dateslider_range = cb_obj.value;

        // extract the start and end datetime from the tuple
        var dateslider_start = dateslider_range[0];
        var dateslider_end = dateslider_range[1];

        var js_start = new Date(dateslider_start);
        var js_end = new Date(dateslider_end);

        js_start.setHours(0,0,0);
        js_end.setHours(23,59,59);

        var one_day=1000*60*60*24;
        var diff_ms = Math.abs(js_end - js_start);
        var diff_day = Math.round(diff_ms/one_day);


        div_3.text = "Range start date: " + js_start.toString();
        div_4.text = "Range end date: " + js_end.toString();
        div_4A.text = "No. of days: " + diff_day;

        var posix_start = js_start.getTime();
        var posix_end = js_end.getTime();

        // update the x-axis range
        plot.extra_x_ranges['datetime_axis_2'].start = posix_start;
        plot.extra_x_ranges['datetime_axis_2'].end = posix_end;

        plot.change.emit();
    """

    # Javascript callback3 for adjusting the datetime x-axis according to the calendar date picker dp1
    callback3 = """
        var datepicker_date = cb_obj.value;

        var start_date = new Date(datepicker_date);
        start_date.setHours(0,0,0);

        var end_date = new Date();
        end_date.setTime(start_date.getTime());
        end_date.setDate(start_date.getDate()+1);

        div_5.text = "Calendar start date: " + start_date.toString() ;
        div_6.text = "Calendar end date: " + end_date.toString();

        var posix_start = start_date.getTime();
        var posix_end = end_date.getTime();

        plot.x_range.start = posix_start;
        plot.x_range.end = posix_end;

        plot.change.emit();
    """

    # Javascript callback4 for adjusting the 2nd datetime x-axis according to the calendar date picker dp2
    callback4 = """
        var datepicker_date = cb_obj.value;

        var start_date = new Date(datepicker_date);
        start_date.setHours(0,0,0);

        var end_date = new Date();
        end_date.setTime(start_date.getTime());
        end_date.setDate(start_date.getDate()+1);

        div_7.text = "Calendar start date: " + start_date.toString() ;
        div_8.text = "Calendar end date: " + end_date.toString();

        var posix_start = start_date.getTime();
        var posix_end = end_date.getTime();

        plot.extra_x_ranges['datetime_axis_2'].start = posix_start;
        plot.extra_x_ranges['datetime_axis_2'].end = posix_end;

        plot.change.emit();
    """

    # range slider for adjusting the EnvTemp y-axis
    rs1 = RangeSlider(start=0, end=50, value=(20,40), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color='red', direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode1))

    # range slider for adjusting the WaterTemp y-axis
    rs2 = RangeSlider(start=0, end=50, value=(20,40), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color='green', direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode2 % ('watertemp_axis','watertemp_axis')))

    rs3 = RangeSlider(start=0, end=100, value=(30,100), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color='orange', direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode2 % ('humidity_axis','humidity_axis')))

    rs4 = RangeSlider(start=0, end=14, value=(4,8), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color='blue', direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode2 % ('waterph_axis','waterph_axis')))

    rs5 = RangeSlider(start=-100, end=100, value=(0,10), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color='black', direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode2 % ('journal_axis','journal_axis')))

    # date range sliders for period to period data comparison
    drs1 = DateRangeSlider(start=date.fromtimestamp(1513094400), end=date.today(), value=(date.fromtimestamp(1513094400), date.today()), step=1, format='%d %b %Y',
                    height=5, width=650, show_value=False, callback=CustomJS(args=dict(plot=p1, div_1=div_1, div_2=div_2, div_2A=div_2A), code=callback1 ))

    drs2 = DateRangeSlider(start=date.fromtimestamp(1513094400), end=date.today(), value=(date.fromtimestamp(1513094400), date.today()), step=1, format='%d %b %Y',
                    height=5, width=650, show_value=False, callback=CustomJS(args=dict(plot=p1, div_3=div_3, div_4=div_4, div_4A=div_4A), code=callback2 ))

    # calendar date pickers for 1-day to 1-day data omparison
    dp1 = DatePicker(value=date.today(), callback=CustomJS(args=dict(plot=p1, div_5=div_5, div_6=div_6), code=callback3 ))

    dp2 = DatePicker(value=date.today(), callback=CustomJS(args=dict(plot=p1, div_7=div_7, div_8=div_8), code=callback4 ))

    # create tabs for slider / calender selection methods
    tab_slider = Panel(child=Column(children=[
                        Row(children=[Column(children=[div_A,div_1,div_2,div_2A,drs1]),Column(children=[div_B,div_3,div_4,div_4A,drs2])]),
                        ]), title="slider")

    tab_calendar = Panel(child=Column(children=[
                            Row(children=[Column(children=[div_C,div_5,div_6,dp1]),Column(children=[div_D,div_7,div_8,dp2])]),
                            ]), title="calendar")

    tabs_picker = Tabs(tabs=[ tab_slider, tab_calendar ])

    plots = Column(children=[
                            Row(children=[rs5,rs1,rs2,p1,rs3,rs4]),
                            tabs_picker,
                            ])

    #Store components
    script, div = components(plots)

    #Feed them to the Django template.
    return render(request, 'trend/all_trend_lines.html', {'script' : script , 'div' : div} )

def all_waterflow(request):
    sensor_list = ["WaterLevelLow", "WaterLevelFull", "IsFilling", "WaterFlowFishTank", "WaterFlowMain", "WaterFlowVertGrow", "WaterFlowHorizGrow"]

    dfs = [] #list for storing panda dataframe
    sources = [] #list for storing Bokeh columndatasource

    for i in range(len(sensor_list)):
        #query for models in database
        sensor_model = apps.get_model("graph", sensor_list[i])
        sensor_query = sensor_model.objects.all().order_by('datetime').reverse()
        sensor_query = sensor_query.values('datetime','value')

        #extract the values inside the queryset and place into the temp dict
        sensor_dict = {'datetimes':[], 'values':[]}

        for j in range(len(sensor_query)):
            sensor_dict['datetimes'].append(sensor_query[j]['datetime'])
            sensor_dict['values'].append(sensor_query[j]['value'])

        #create a pandas dataframe using the temp dict, name the columns, convert the timezone
        df = pd.DataFrame(data=sensor_dict, columns=['datetimes','values'])
        dfs.append(df)
        dfs[i].datetimes = pd.DatetimeIndex(pd.to_datetime(dfs[i].datetimes)).tz_convert(pytz.timezone('Asia/Singapore'))
        dfs[i].datetimes.tolist()

        #create a bokeh columndatasource
        source = ColumnDataSource(data=dict(datetimes=dfs[i]['datetimes'], values=dfs[i]['values']))
        sources.append(source)
        sources[i].add(dfs[i]['datetimes'].apply(lambda d: d.strftime('%Y-%m-%d, %H:%M:%S')), 'datetimes_formatted')

    # query for data from the model in the Journal app
    journal_model = apps.get_model("journal", "Post")
    journal_query = journal_model.objects.all().order_by('published_date').reverse()
    journal_query = journal_query.values('published_date','title', 'text', 'value')

    #extract the values inside the queryset and place into a temporary journal_dict
    journal_dict = {'published_date':[], 'title':[], 'text':[], 'value':[]}

    for j in range(len(journal_query)):
        journal_dict['published_date'].append(journal_query[j]['published_date'])
        journal_dict['title'].append(journal_query[j]['title'])
        journal_dict['text'].append(journal_query[j]['text'])
        journal_dict['value'].append(journal_query[j]['value'])

    #create a pandas dataframe using the temporary journal_dict, name the columns, convert the timezone
    df2 = pd.DataFrame(data=journal_dict, columns=['published_date','title','text', 'value'])
    df2.published_date = pd.DatetimeIndex(pd.to_datetime(df2.published_date)).tz_convert(pytz.timezone('Asia/Singapore'))
    df2.published_date.tolist()

    #create a bokeh columndatasource for data in the Journal app
    source2 = ColumnDataSource(data=dict(published_date=df2['published_date'], title=df2['title'], text=df2['text'], value=df2['value']))

    #add a column in the columndatasource with formatted datetime
    source2.add(df2['published_date'].apply(lambda d: d.strftime('%Y-%m-%d, %H:%M:%S')), 'published_date_formatted')

    # create a new plot with a datetime axis type
    p1 = figure(plot_width=1200, plot_height=500, x_axis_type="datetime", y_range=(-1,2),
                x_range=Range1d(start=datetime.fromtimestamp(1513094400), end=datetime.now(tz=pytz.timezone('Asia/Singapore'))),
                tools=[WheelZoomTool(), PanTool(), ResetTool(), BoxZoomTool(), SaveTool(), UndoTool(), RedoTool(), CrosshairTool()],
                title="Data for Water Flow ")

    # set x-axis label
    p1.xaxis.axis_label = 'Date & Time for 1st Graph'

    # set y-axis label
    p1.yaxis.axis_label = 'Sensor On/Off'

    # set extra y-axes label and range
    p1.extra_y_ranges = {"flowrate_axis": Range1d(start=-10, end=200),
                         "journal_axis": Range1d(start=-100, end=100)}

    # create 2nd datetime x-axis so that graphs can be separated
    p1.extra_x_ranges = {"datetime_axis_2": Range1d(start=datetime.fromtimestamp(1513094400), end=datetime.now(tz=pytz.timezone('Asia/Singapore')))}

    # add 2nd y-axis to the plot.
    p1.add_layout(LinearAxis(y_range_name="flowrate_axis", axis_label='flowrate [L/min]'), 'right')
    p1.add_layout(LinearAxis(y_range_name="journal_axis", axis_label='Journal'), 'left')

    # add 2nd datetime x-axis to the plot
    p1.add_layout(DatetimeAxis(x_range_name="datetime_axis_2", axis_label='Date & Time for 2nd Graph'), 'below')

    # glyph for WaterLevelLow 1st graph
    g1 = Line(x='datetimes', y='values', line_color='Grey', line_alpha=1)
    # glyph for WaterLevelLow 2nd graph
    g2 = Line(x='datetimes', y='values', line_color='gold', line_alpha=1)
    # glyph for WaterLevelFull 1st graph
    g3 = Line(x='datetimes', y='values', line_color='Purple', line_alpha=1)
    # glyph for WaterLevelFull 2nd graph
    g4 = Line(x='datetimes', y='values', line_color='deeppink', line_alpha=1)
    # glyph for IsFilling 1st graph
    g5 = Line(x='datetimes', y='values', line_color='Green', line_alpha=1)
    # glyph for IsFilling 2nd graph
    g6 = Line(x='datetimes', y='values', line_color='navy', line_alpha=1)
    # glyph for WaterFlowFishTank 1st graph
    g7 = Line(x='datetimes', y='values', line_color='Crimson', line_alpha=1)
    # glyph for WaterFlowFishTank 2nd graph
    g8 = Line(x='datetimes', y='values', line_color='indigo', line_alpha=1)
    # glyph for WaterFlowMain 1st graph
    g9 = Line(x='datetimes', y='values', line_color='Coral', line_alpha=1)
    # glyph for WaterFlowMain 2nd graph
    g10 = Line(x='datetimes', y='values', line_color='green', line_alpha=1)
    # glyph for WaterFlowVertGrow 1st graph
    g11 = Line(x='datetimes', y='values', line_color='Indigo', line_alpha=1)
    # glyph for WaterFlowVertGrow 2nd graph
    g12 = Line(x='datetimes', y='values', line_color='green', line_alpha=1)
    # glyph for WaterFlowHorizGrow 1st graph
    g13 = Line(x='datetimes', y='values', line_color='pink', line_alpha=1)
    # glyph for WaterFlowHorizGrow 2nd graph
    g14 = Line(x='datetimes', y='values', line_color='Steelblue', line_alpha=1)
    # glyph for Journal entries
    g15 = Circle(x='published_date', y='value', fill_color='black', fill_alpha=1)

    # create the respective renderers
    g1_r = p1.add_glyph(source_or_glyph=sources[0], glyph=g1)
    g2_r = p1.add_glyph(source_or_glyph=sources[0], glyph=g2, x_range_name="datetime_axis_2")
    g3_r = p1.add_glyph(source_or_glyph=sources[1], glyph=g3)
    g4_r = p1.add_glyph(source_or_glyph=sources[1], glyph=g4, x_range_name="datetime_axis_2")
    g5_r = p1.add_glyph(source_or_glyph=sources[2], glyph=g5)
    g6_r = p1.add_glyph(source_or_glyph=sources[2], glyph=g6, x_range_name="datetime_axis_2")
    g7_r = p1.add_glyph(source_or_glyph=sources[3], glyph=g7, y_range_name="flowrate_axis")
    g8_r = p1.add_glyph(source_or_glyph=sources[3], glyph=g8, y_range_name="flowrate_axis", x_range_name="datetime_axis_2")
    g9_r = p1.add_glyph(source_or_glyph=sources[4], glyph=g9, y_range_name="flowrate_axis")
    g10_r = p1.add_glyph(source_or_glyph=sources[4], glyph=g10, y_range_name="flowrate_axis", x_range_name="datetime_axis_2")
    g11_r = p1.add_glyph(source_or_glyph=sources[5], glyph=g11, y_range_name="flowrate_axis")
    g12_r = p1.add_glyph(source_or_glyph=sources[5], glyph=g12, y_range_name="flowrate_axis", x_range_name="datetime_axis_2")
    g13_r = p1.add_glyph(source_or_glyph=sources[6], glyph=g13, y_range_name="flowrate_axis")
    g14_r = p1.add_glyph(source_or_glyph=sources[6], glyph=g14, y_range_name="flowrate_axis", x_range_name="datetime_axis_2")
    g15_r = p1.add_glyph(source_or_glyph=source2, glyph=g15, y_range_name="journal_axis")

    # create a hover tool for all line glyphs
    gall_hover = HoverTool(renderers=[g1_r,g2_r,g3_r,g4_r,g5_r,g6_r,g7_r,g8_r,g9_r,g10_r,g11_r,g12_r,g13_r,g14_r],
            tooltips=[
                ('value', '@values{0.00}'),
                ('date', '@datetimes_formatted'),
            ]
        )

    # create a hover tool for circle glyph
    g15_hover = HoverTool(renderers=[g15_r],
            tooltips=[
                ('published_date', '@published_date_formatted'),
                ('title', '@title'),
                ('text', '@text'),
                ('journal value', '@value'),
            ]
        )

    # add the hover tools to the plot
    p1.add_tools(gall_hover)
    p1.add_tools(g15_hover)

    #create interactive legends
    legend = Legend(items=[
    ("WaterLevelLow 1", [g1_r]),
    ("WaterLevelLow 2", [g2_r]),
    ("WaterLevelFull 1", [g3_r]),
    ("WaterLevelFull 2", [g4_r]),
    ("IsFilling 1", [g5_r]),
    ("IsFilling 2", [g6_r]),
    ("WaterFlowFishTank 1", [g7_r]),
    ("WaterFlowFishTank 2", [g8_r]),
    ("WaterFlowMain 1", [g9_r]),
    ("WaterFlowMain 2", [g10_r]),
    ("WaterFlowVertGrow 1", [g11_r]),
    ("WaterFlowVertGrow 2", [g12_r]),
    ("WaterFlowHorizGrow 1", [g13_r]),
    ("WaterFlowHorizGrow 2", [g14_r]),
    ("Journal", [g15_r]),
    ], location=(0, 0), click_policy='hide')

    # add legend to plots
    p1.add_layout(legend, 'right')

    #Javascript code to format the datetime x-axis to localize the datetimes manually using this workaround
    datetime_formatter="""
        //var sg_date = new Date(tick).toLocaleString("en-US", {timeZone: "Asia/Singapore"})
        var timestring = tick;
        var locale_date = new Date(timestring).toLocaleDateString();
        var locale_time = new Date(timestring).toLocaleTimeString();
        var locale_datetime = locale_date + " " + locale_time;
        return locale_datetime
    """
    p1.xaxis.formatter = FuncTickFormatter(code=datetime_formatter)

    #create a y-axis range slider for better visibility during analysis
    jscode1="""
        //cb_obj.value refers to the rangeslider's value, which is a tuple containing 2 values, assign this to y_range
        var y_range = cb_obj.value;

        //first item of y_range is the min value, second item is the max value
        var y_min = y_range[0];
        var y_max = y_range[1];

        //update the start and end of the plot's range
        plot.y_range.start = y_min;
        plot.y_range.end = y_max;
        plot.change.emit();
    """

    jscode2="""
        //cb_obj.value refers to the rangeslider's value, which is a tuple containing 2 values, assign this to y_range
        var y_range = cb_obj.value;

        //first item of y_range is the min value, second item is the max value
        var y_min = y_range[0];
        var y_max = y_range[1];

        //update the plot's extra_y_ranges, the variables are passed in when calling out RangeSlider
        plot.extra_y_ranges['%s'].start = y_min;
        plot.extra_y_ranges['%s'].end = y_max;
        plot.change.emit();
    """

    div_1 = Div(text="""Range start date: """, width=800, height=5)
    div_2 = Div(text="""Range end date: """, width=800, height=5)
    div_2A = Div(text="""No. of days: """, width=800, height=5)
    div_3 = Div(text="""Range start date: """, width=800, height=5)
    div_4 = Div(text="""Range end date: """, width=800, height=5)
    div_4A = Div(text="""No. of days: """, width=800, height=5)
    div_5 = Div(text="""Calendar start date: """, width=800, height=5)
    div_6 = Div(text="""Calendar end date: """, width=800, height=5)
    div_7 = Div(text="""Calendar start date: """, width=800, height=5)
    div_8 = Div(text="""Calendar end date: """, width=800, height=5)

    div_A = Div(text="""Graph 1""", width=800, height=5)
    div_B = Div(text="""Graph 2""", width=800, height=5)
    div_C = Div(text="""Graph 1""", width=800, height=5)
    div_D = Div(text="""Graph 2""", width=800, height=5)

    # Javascript callback1 for adjusting the datetime x-axis according to the date range slider drs1
    callback1 = """
        // cb_obj refers to the date range slider, which has attribute "value" in the form of tuple
        var dateslider_range = cb_obj.value;

        // extract the start and end datetime from the tuple
        var dateslider_start = dateslider_range[0];
        var dateslider_end = dateslider_range[1];

        var js_start = new Date(dateslider_start);
        var js_end = new Date(dateslider_end);

        js_start.setHours(0,0,0);
        js_end.setHours(23,59,59);

        var one_day=1000*60*60*24;
        var diff_ms = Math.abs(js_end - js_start);
        var diff_day = Math.round(diff_ms/one_day);

        div_1.text = "Range start date: " + js_start.toString() ;
        div_2.text = "Range end date: " + js_end.toString();
        div_2A.text = "No. of days: " + diff_day;

        var posix_start = js_start.getTime();
        var posix_end = js_end.getTime();

        // update the x-axis range
        plot.x_range.start = posix_start;
        plot.x_range.end = posix_end;

        plot.change.emit();
    """

    # Javascript callback2 for adjusting the 2nd datetime x-axis according to the date range slider drs2
    callback2 = """
        // cb_obj refers to the date range slider, which has attribute "value" in the form of tuple
        var dateslider_range = cb_obj.value;

        // extract the start and end datetime from the tuple
        var dateslider_start = dateslider_range[0];
        var dateslider_end = dateslider_range[1];

        var js_start = new Date(dateslider_start);
        var js_end = new Date(dateslider_end);

        js_start.setHours(0,0,0);
        js_end.setHours(23,59,59);

        var one_day=1000*60*60*24;
        var diff_ms = Math.abs(js_end - js_start);
        var diff_day = Math.round(diff_ms/one_day);


        div_3.text = "Range start date: " + js_start.toString();
        div_4.text = "Range end date: " + js_end.toString();
        div_4A.text = "No. of days: " + diff_day;

        var posix_start = js_start.getTime();
        var posix_end = js_end.getTime();

        // update the x-axis range
        plot.extra_x_ranges['datetime_axis_2'].start = posix_start;
        plot.extra_x_ranges['datetime_axis_2'].end = posix_end;

        plot.change.emit();
    """

    # Javascript callback3 for adjusting the datetime x-axis according to the calendar date picker dp1
    callback3 = """
        var datepicker_date = cb_obj.value;

        var start_date = new Date(datepicker_date);
        start_date.setHours(0,0,0);

        var end_date = new Date();
        end_date.setTime(start_date.getTime());
        end_date.setDate(start_date.getDate()+1);

        div_5.text = "Calendar start date: " + start_date.toString() ;
        div_6.text = "Calendar end date: " + end_date.toString();

        var posix_start = start_date.getTime();
        var posix_end = end_date.getTime();

        plot.x_range.start = posix_start;
        plot.x_range.end = posix_end;

        plot.change.emit();
    """

    # Javascript callback4 for adjusting the 2nd datetime x-axis according to the calendar date picker dp2
    callback4 = """
        var datepicker_date = cb_obj.value;

        var start_date = new Date(datepicker_date);
        start_date.setHours(0,0,0);

        var end_date = new Date();
        end_date.setTime(start_date.getTime());
        end_date.setDate(start_date.getDate()+1);

        div_7.text = "Calendar start date: " + start_date.toString() ;
        div_8.text = "Calendar end date: " + end_date.toString();

        var posix_start = start_date.getTime();
        var posix_end = end_date.getTime();

        plot.extra_x_ranges['datetime_axis_2'].start = posix_start;
        plot.extra_x_ranges['datetime_axis_2'].end = posix_end;

        plot.change.emit();
    """

    # range slider for adjusting the on/off y-axis
    rs1 = RangeSlider(start=-1, end=2, value=(0,1), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color='Grey', direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode1))

    # range slider for adjusting the flowrate y-axis
    rs2 = RangeSlider(start=-10, end=200, value=(0,12), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color='Crimson', direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode2 % ('flowrate_axis','flowrate_axis')))

    # range slider for adjusting the journal y-axis
    rs3 = RangeSlider(start=-100, end=100, value=(0,10), step=1, orientation="vertical", height=400, width=60, show_value=False, bar_color='black', direction="rtl",
                    callback=CustomJS(args=dict(plot=p1), code=jscode2 % ('journal_axis','journal_axis')))

    # date range sliders for period to period data comparison
    drs1 = DateRangeSlider(start=date.fromtimestamp(1513094400), end=date.today(), value=(date.fromtimestamp(1513094400), date.today()), step=1, format='%d %b %Y',
                    height=5, width=650, show_value=False, callback=CustomJS(args=dict(plot=p1, div_1=div_1, div_2=div_2, div_2A=div_2A), code=callback1 ))

    drs2 = DateRangeSlider(start=date.fromtimestamp(1513094400), end=date.today(), value=(date.fromtimestamp(1513094400), date.today()), step=1, format='%d %b %Y',
                    height=5, width=650, show_value=False, callback=CustomJS(args=dict(plot=p1, div_3=div_3, div_4=div_4, div_4A=div_4A), code=callback2 ))

    # calendar date pickers for 1-day to 1-day data omparison
    dp1 = DatePicker(value=date.today(), callback=CustomJS(args=dict(plot=p1, div_5=div_5, div_6=div_6), code=callback3 ))

    dp2 = DatePicker(value=date.today(), callback=CustomJS(args=dict(plot=p1, div_7=div_7, div_8=div_8), code=callback4 ))

    # create tabs for slider / calender selection methods
    tab_slider = Panel(child=Column(children=[
                        Row(children=[Column(children=[div_A,div_1,div_2,div_2A,drs1]),Column(children=[div_B,div_3,div_4,div_4A,drs2])]),
                        ]), title="slider")

    tab_calendar = Panel(child=Column(children=[
                            Row(children=[Column(children=[div_C,div_5,div_6,dp1]),Column(children=[div_D,div_7,div_8,dp2])]),
                            ]), title="calendar")

    tabs_picker = Tabs(tabs=[ tab_slider, tab_calendar ])

    plots = Column(children=[
                            Row(children=[rs3,rs1,p1,rs2]),
                            tabs_picker,
                            ])

    #Store components
    script, div = components(plots)

    #Feed them to the Django template.
    return render(request, 'trend/all_waterflow.html', {'script' : script , 'div' : div} )

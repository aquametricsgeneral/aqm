
var gauge_1 = document.getElementById('gauge_1');
var gauge_2 = document.getElementById('gauge_2');
var gauge_3 = document.getElementById('gauge_3');
var gauge_4 = document.getElementById('gauge_4');
var gauge_5 = document.getElementById('gauge_5');
var gauge_6 = document.getElementById('gauge_6');
var gauge_7 = document.getElementById('gauge_7');
var gauge_8 = document.getElementById('gauge_8');
var gauge_9 = document.getElementById('gauge_9');
var gauge_10 = document.getElementById('gauge_10');

updateGauge('EnvTemp', gauge_1);
updateGauge('WaterTempFishTank', gauge_2);
updateGauge('WaterPH', gauge_3);
updateGauge('EnvHumidity', gauge_4);
updateGauge('WaterFlowMain', gauge_5);
updateGauge('WaterFlowFishTank', gauge_6);
updateGauge('WaterFlowVertGrow', gauge_7);
updateGauge('WaterFlowHorizGrow', gauge_8);
checkWaterLevel(gauge_9);
checkSystemStatus(gauge_10);
updateLastUpdated('last-updated');

setInterval(function(){
  updateGauge('EnvTemp', gauge_1);
  updateGauge('WaterTempFishTank', gauge_2);
  updateGauge('WaterPH', gauge_3);
  updateGauge('EnvHumidity', gauge_4);
  updateGauge('WaterFlowMain', gauge_5);
  updateGauge('WaterFlowFishTank', gauge_6);
  updateGauge('WaterFlowVertGrow', gauge_7);
  updateGauge('WaterFlowHorizGrow', gauge_8);
  checkWaterLevel(gauge_9);
  checkSystemStatus(gauge_10);
  updateLastUpdated('last-updated');
}, 30000);

$( "#last-updated").toggleClass("loading");
$( document ).ajaxStart(function() {
  $( "#last-updated").toggleClass("loading");
}).ajaxStop(function() {
  $( "#last-updated").toggleClass("loading");
});

function updateGauge(sensor_id, gauge_id) {
        $.ajax({
            type: "GET",
            url: "/dashboard/ajax_data_for_gauge/",
            dataType: "json",
            data: {'sensor_id': sensor_id},
        }).done(function(result){
            var jsonData = result;
            var gaugeValue = jsonData['gauge_value'];
            //console.log(gaugeValue);
            var lowerlimit = jsonData['lowerlimit'];
            var upperlimit = jsonData['upperlimit'];
            var limits = [{from: parseFloat(lowerlimit), to: parseFloat(upperlimit), color: "rgb(153, 255, 153)"}];
            var data_highlights = JSON.stringify(limits);
            //console.log(data_highlights);
            gauge_id.setAttribute('data-value', gaugeValue);
            gauge_id.setAttribute('data-highlights', data_highlights);
        });
}

function checkWaterLevel(gauge_id) {
        $.ajax({
            type: "GET",
            url: "/monitor/waterlevel_status/",
            dataType: "json",
        }).done(function(result){
            var jsonData = result;
            var gaugeValue = jsonData['waterlevel_value']
            //console.log(gaugeValue);
            gauge_id.setAttribute('data-value', gaugeValue);
        });
}

function checkSystemStatus(gauge_id) {
        $.ajax({
            type: "GET",
            url: "/monitor/system_status/",
            dataType: "json",
        }).done(function(result){
            var jsonData = result;
            var gaugeValue = jsonData['System Status']
            gauge_id.setAttribute('data-value', gaugeValue);
        });
}

function updateLastUpdated(div_id) {
        $.ajax({
            type: "GET",
            url: "/monitor/system_status/",
            dataType: "json",
        }).done(function(result){
            var jsonData = result;
            var lastUpdated = jsonData['Last Updated']
            document.getElementById(div_id).innerHTML=' Updated: ' + lastUpdated;
        });
}

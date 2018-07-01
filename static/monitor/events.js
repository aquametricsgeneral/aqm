updateLastUpdated('monitor-last-updated');

var table = $('#statusTable').DataTable({
            "ajax": {
                url: '/monitor/events_ajax',
                dataSrc: ''
            },
            "columns": [
              { "data": 'sensor' },
              { "data": 'alert'},
              { "data": 'datetime' },
              { "data": 'value' },
              { "data": 'lowerlimit' },
              { "data": 'upperlimit' },
              { "data": 'withinlimit' },
            ],
            "columnDefs": [
                {
                    "render": function (data, type, row) {
                        return (data === 'True') ? '<span class="fas fa-bell text-success"></span>' :
                        '<span class="fas fa-bell-slash text-secondary"></span>';
                    },
                    "targets": 1
                },
                {
                    "render": function (data, type, row) {
                        return (data === 'True') ? '<span class="fas fa-check-circle text-success"></span>' :
                        '<span class="fas fa-exclamation-circle text-danger"></span>';
                    },
                    "targets": 6
                },
                {
                    "render": function (data, type, row) {

                      switch (data) {
                        case 'EnvTemp':
                          data = '<span class="fas fa-thermometer-half mr-1" style="color: #1380FC"></span>Temperature - Air';
                          break;

                        case 'WaterTempFishTank':
                          data = '<span class="fas fa-thermometer-half mr-1" style="color: #1380FC"></span>Temperature - Fish Tank';
                          break;

                        case 'WaterTempSumpTank':
                          data = '<span class="fas fa-thermometer-half mr-1" style="color: #1380FC"></span>Temperature - Sump Tank';
                          break;

                        case 'EnvHumidity':
                          data = '<span class="fas fa-cloud mr-1" style="color: #1380FC"></span>Humidity';
                          break;

                        case 'WaterPH':
                          data = '<span class="fas fa-vial mr-1" style="color: #1380FC"></span>Water pH';
                          break;

                        case 'WaterFlowMain':
                          data = '<span class="fas fa-tint mr-1" style="color: #1380FC"></span>Flow - Main';
                          break;

                        case 'WaterFlowFishTank':
                          data = '<span class="fas fa-tint mr-1" style="color: #1380FC"></span>Flow - Fish Tank';
                          break;

                        case 'WaterFlowHorizGrow':
                          data = '<span class="fas fa-tint mr-1" style="color: #1380FC"></span>Flow - Horizontal';
                          break;

                        case 'WaterFlowVertGrow':
                          data = '<span class="fas fa-tint mr-1" style="color: #1380FC"></span>Flow - Vertical';
                          break;

                        case 'IsFilling':
                          data = '<span class="fas fa-filter mr-1" style="color: #1380FC"></span>Water Filling';
                          break;

                        default:
                          console.log("Error");
                        };

                        return data;
                },
                "targets": 0
              }
            ],
            "paging": false,
            "searching": false,
            "bInfo" : false
          });

setInterval(function(){
    console.log('reloading');
    table.ajax.reload();
    updateLastUpdated('monitor-last-updated');
}, 30000);

$( "#monitor-last-updated").toggleClass("loading");
$( document ).ajaxStart(function() {
  $( "#monitor-last-updated").toggleClass("loading");
}).ajaxStop(function() {
  $( "#monitor-last-updated").toggleClass("loading");
});

function updateLastUpdated(div_id) {
        $.ajax({
            type: "GET",
            url: "/monitor/monitor_status/",
            dataType: "json",
        }).done(function(result){
            var jsonData = result;
            var lastUpdated = jsonData['Last Updated']
            document.getElementById(div_id).innerHTML=' Updated: ' + lastUpdated;
        });
}

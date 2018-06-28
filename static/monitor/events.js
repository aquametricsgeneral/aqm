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
                          data = 'Air Temperature';
                          break;

                        case 'WaterTempFishTank':
                          data = 'Fish Tank Temperature';
                          break;

                        case 'WaterTempSumpTank':
                          data = 'Sump Tank Temperature';
                          break;

                        case 'EnvHumidity':
                          data = 'Humidity';
                          break;

                        case 'WaterPH':
                          data = 'Water pH';
                          break;

                        case 'WaterFlowMain':
                          data = 'Main Flow';
                          break;

                        case 'WaterFlowFishTank':
                          data = 'Fish Tank Flow';
                          break;

                        case 'WaterFlowHorizGrow':
                          data = 'Horizontal Flow';
                          break;

                        case 'WaterFlowVertGrow':
                          data = 'Vertical Flow';
                          break;

                        case 'IsFilling':
                          data = 'Water Filling';
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

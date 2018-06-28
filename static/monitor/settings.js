// each sensor is ordered according to the 'order' field in the model, variables below are hardcoded according to the 'order' field
var EnvTemp_order = "0";
var WaterTempFishTank_order = "1";
var WaterTempSumpTank_order = "2";
var EnvHumidity_order = "3";
var WaterPH_order = "4";
var IsFilling_order = "5";
var WaterFlowMain_order = "6";
var WaterFlowFishTank_order = "7";
var WaterFlowVertGrow_order = "8";
var WaterFlowHorizGrow_order = "9";

// function for creating slider, takes in specific parameters for the particular slider
function createSlider(slider_id, lowerlimit_id, upperlimit_id, min, max, from, to, step, postfix) {
  $(slider_id).ionRangeSlider({
  type: "double",
  min: min,
  max: max,
  from: $(lowerlimit_id).val(),
  to: $(upperlimit_id).val(),
  step: step,
  postfix: postfix,
  force_edges: true,
  onChange: function (data) {
      var from = $(slider_id).data('from');
      var to = $(slider_id).data('to');
      $(lowerlimit_id).val(from)
      $(upperlimit_id).val(to)
   }
  });
}

$("#id_form-5-slider").hide();
$("#last_saved_5").hide();
$("#last_saved_5").prev().hide();

// call the function to create sliders
createSlider("#id_form-"+EnvTemp_order+"-slider", "#id_form-"+EnvTemp_order+"-lowerlimit", "#id_form-"+EnvTemp_order+"-upperlimit", 10, 50, 20, 30, 1, " °C");
createSlider("#id_form-"+WaterTempFishTank_order+"-slider", "#id_form-"+WaterTempFishTank_order+"-lowerlimit", "#id_form-"+WaterTempFishTank_order+"-upperlimit", 10, 50, 20, 30, 1, " °C");
createSlider("#id_form-"+WaterTempSumpTank_order+"-slider", "#id_form-"+WaterTempSumpTank_order+"-lowerlimit", "#id_form-"+WaterTempSumpTank_order+"-upperlimit", 10, 50, 20, 30, 1, " °C");
createSlider("#id_form-"+EnvHumidity_order+"-slider", "#id_form-"+EnvHumidity_order+"-lowerlimit", "#id_form-"+EnvHumidity_order+"-upperlimit", 10, 100, 50, 80, 1, " %");
createSlider("#id_form-"+WaterPH_order+"-slider", "#id_form-"+WaterPH_order+"-lowerlimit", "#id_form-"+WaterPH_order+"-upperlimit", 0, 14, 5, 7, 1, "");
//createSlider("#id_form-"+IsFilling_order+"-slider", "#id_form-"+IsFilling_order+"-lowerlimit", "#id_form-"+IsFilling_order+"-upperlimit", 0, 1, 0, 0, 1, "");
createSlider("#id_form-"+WaterFlowMain_order+"-slider", "#id_form-"+WaterFlowMain_order+"-lowerlimit", "#id_form-"+WaterFlowMain_order+"-upperlimit", 0, 20, 1, 10, 1, "");
createSlider("#id_form-"+WaterFlowFishTank_order+"-slider", "#id_form-"+WaterFlowFishTank_order+"-lowerlimit", "#id_form-"+WaterFlowFishTank_order+"-upperlimit", 0, 20, 1, 10, 1, "");
createSlider("#id_form-"+WaterFlowVertGrow_order+"-slider", "#id_form-"+WaterFlowVertGrow_order+"-lowerlimit", "#id_form-"+WaterFlowVertGrow_order+"-upperlimit", 0, 40, 2, 20, 1, "");
createSlider("#id_form-"+WaterFlowHorizGrow_order+"-slider", "#id_form-"+WaterFlowHorizGrow_order+"-lowerlimit", "#id_form-"+WaterFlowHorizGrow_order+"-upperlimit", 0, 40, 1, 30, 1, "");

// to display static values of lowerlimit and upperlimit that's last retrieved from the database
for(i=0;i<10;i++) {

  if (i<5) {
    var lowerlimit = Math.ceil($("#id_form-"+i+"-lowerlimit").val());
    var upperlimit = Math.ceil($("#id_form-"+i+"-upperlimit").val());
    var unit = $("#id_form-"+i+"-slider").data('ionRangeSlider').options.postfix;
    $("#last_saved_"+i).html(" Last Saved: " + lowerlimit + " " + unit + " - " + upperlimit + " " + unit);
  } else if (i>5) {
    var lowerlimit = Math.ceil($("#id_form-"+i+"-lowerlimit").val());
    var upperlimit = Math.ceil($("#id_form-"+i+"-upperlimit").val());
    var unit = $("#id_form-"+i+"-slider").data('ionRangeSlider').options.postfix;
    $("#last_saved_"+i).html(" Last Saved: " + lowerlimit + " " + unit + " - " + upperlimit + " " + unit);
  }

};


// SweetAlert pop ups when the variable saved_alert received changes from 0 to 1
$(document).ready(function() {
  if (document.forms["setting_form"]["saved_alert"].value==1){
    swal("OK!", "New settings saved.", "success")
  }
  if (document.forms["setting_form"]["saved_alert"].value==0){
    swal("Oops!", "There are errors.", "error")
  }
});

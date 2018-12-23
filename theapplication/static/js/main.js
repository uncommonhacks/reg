// Materialize JQuery Initialization
$(document).ready(function(){
  $("select").filter((e) => e != 2).formSelect();

  let schoolSelect = $("select[name=school]");
  schoolSelect.select2({width: "100%"});

  $("select").change(function(e) {
    console.log("selectchagnevent", e);
  });
});

// Materialize JQuery Initialization
$(document).ready(function(){

  $("select").filter((e) => e != 2).formSelect();

  let schoolSelect = $("select[name=school]");
  schoolSelect.select2({width: "100%"});


  let minimizeDropdowns = function (){
      console.log("minimizing dropdowns");
      let selectDropdowns =  Array.prototype.slice.call(document.getElementsByClassName("dropdown-content"), 0);
      let select2Dropdowns =  Array.prototype.slice.call(document.getElementsByClassName("select2-dropdown"), 0);
      let dropdowns = selectDropdowns.concat(select2Dropdowns);
      for(let i = 0; i < dropdowns.length; i++){
          dropdowns[i].style.display = "none";
      }
  };

  document.addEventListener("click", minimizeDropdowns);
  
 
});

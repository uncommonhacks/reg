// Materialize JQuery Initialization
$(document).ready(function(){

  $("select").filter((e) => e != 2).formSelect();

  let schoolSelect = $("select[name=school]");
  schoolSelect.select2({width: "100%"});

  let schoolDropdownOpen = false;

  $("select[name=school]").on("select2:open", function (e) {
    schoolDropdownOpen = true;
  });

  $("select[name=school]").on("select2:close", function (e) {
    schoolDropdownOpen = false;
  });

  let closeDropdowns = function(){
    let selects = $("select");
    for (let i = 0; i < selects.length; i++) {
      let formInstance = M.FormSelect.getInstance(selects[i]);
      if (formInstance && formInstance.dropdown && formInstance.dropdown.isOpen) {
        formInstance.dropdown.close();
      }
    }

    if (schoolDropdownOpen) {
      $("select[name=school]").select2("close");
    }
  };

  $(window).click(function (){
    closeDropdowns();
  });

  $(".input-field").click(function (e) {
    e.stopPropagation();
  });
});

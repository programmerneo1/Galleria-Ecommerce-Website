$(document).ready(function() {
    $("#sidebarCollapse").on("click", function() {
      $("#sidebar").addClass("active");
    });
  
    $("#sidebarCollapseX").on("click", function() {
      $("#sidebar").removeClass("active");
    });
    
    // handling the bottom line color
    $("#navlink1").on("click", function() {
      if ($("#navlink1").hasClass("active")) {
        $("#navlink1").removeClass("active");
      }
      if ($("#navlink2").hasClass("active")) {
        $("#navlink2").removeClass("active");
      }
      if ($("#navlink3").hasClass("active")) {
        $("#navlink3").removeClass("active");
      }if ($("#navlink4").hasClass("active")) {
        $("#navlink4").removeClass("active");
      }if ($("#navlink5").hasClass("active")) {
        $("#navlink5").removeClass("active");
      }if ($("#navlink6").hasClass("active")) {
        $("#navlink6").removeClass("active");
      }
      $("#navlink1").addClass("active");
    });

    $("#navlink2").on("click", function() {
      if ($("#navlink1").hasClass("active")) {
        $("#navlink1").removeClass("active");
      }
      if ($("#navlink2").hasClass("active")) {
        $("#navlink2").removeClass("active");
      }
      if ($("#navlink3").hasClass("active")) {
        $("#navlink3").removeClass("active");
      }if ($("#navlink4").hasClass("active")) {
        $("#navlink4").removeClass("active");
      }if ($("#navlink5").hasClass("active")) {
        $("#navlink5").removeClass("active");
      }if ($("#navlink6").hasClass("active")) {
        $("#navlink6").removeClass("active");
      }
      $("#navlink2").addClass("active");
    });
    
    $("#navlink3").on("click", function() {
      if ($("#navlink1").hasClass("active")) {
        $("#navlink1").removeClass("active");
      }
      if ($("#navlink2").hasClass("active")) {
        $("#navlink2").removeClass("active");
      }
      if ($("#navlink3").hasClass("active")) {
        $("#navlink3").removeClass("active");
      }if ($("#navlink4").hasClass("active")) {
        $("#navlink4").removeClass("active");
      }if ($("#navlink5").hasClass("active")) {
        $("#navlink5").removeClass("active");
      }if ($("#navlink6").hasClass("active")) {
        $("#navlink6").removeClass("active");
      }
      $("#navlink3").addClass("active");
    });
  
    $("#navlink4").on("click", function() {
      if ($("#navlink1").hasClass("active")) {
        $("#navlink1").removeClass("active");
      }
      if ($("#navlink2").hasClass("active")) {
        $("#navlink2").removeClass("active");
      }
      if ($("#navlink3").hasClass("active")) {
        $("#navlink3").removeClass("active");
      }if ($("#navlink4").hasClass("active")) {
        $("#navlink4").removeClass("active");
      }if ($("#navlink5").hasClass("active")) {
        $("#navlink5").removeClass("active");
      }if ($("#navlink6").hasClass("active")) {
        $("#navlink6").removeClass("active");
      }
      $("#navlink4").addClass("active");
    });
    
    $("#navlink5").on("click", function() {
      if ($("#navlink1").hasClass("active")) {
        $("#navlink1").removeClass("active");
      }
      if ($("#navlink2").hasClass("active")) {
        $("#navlink2").removeClass("active");
      }
      if ($("#navlink3").hasClass("active")) {
        $("#navlink3").removeClass("active");
      }if ($("#navlink4").hasClass("active")) {
        $("#navlink4").removeClass("active");
      }if ($("#navlink5").hasClass("active")) {
        $("#navlink5").removeClass("active");
      }if ($("#navlink6").hasClass("active")) {
        $("#navlink6").removeClass("active");
      }
      $("#navlink5").addClass("active");
    });

    $("#navlink6").on("click", function() {
      if ($("#navlink1").hasClass("active")) {
        $("#navlink1").removeClass("active");
      }
      if ($("#navlink2").hasClass("active")) {
        $("#navlink2").removeClass("active");
      }
      if ($("#navlink3").hasClass("active")) {
        $("#navlink3").removeClass("active");
      }if ($("#navlink4").hasClass("active")) {
        $("#navlink4").removeClass("active");
      }if ($("#navlink5").hasClass("active")) {
        $("#navlink5").removeClass("active");
      }if ($("#navlink6").hasClass("active")) {
        $("#navlink6").removeClass("active");
      }
      $("#navlink6").addClass("active");
    });

      // end of bottom line color control

    $("#sidebarCollapse").on("click", function() {
      if ($("#sidebar").hasClass("active")) {
        $(".overlay").addClass("visible");
        console.log("it's working!");
      }
    });
  
    $("#sidebarCollapseX").on("click", function() {
      $(".overlay").removeClass("visible");
    });


    $("#aboutbutton").on("click", function() {
      if ($("#about").hasClass("is-active")) {
      $("#about").removeClass("is-active");
    }if ($("#experience").hasClass("is-active")) {
      $("#experience").removeClass("is-active");
    }if ($("#contact").hasClass("is-active")) {
      $("#contact").removeClass("is-active");
    }
    $("#about").addClass("is-active");
  });

  $("#experiencebutton").on("click", function() {
      console.log("Clicked");
      if ($("#about").hasClass("is-active")) {
      $("#about").removeClass("is-active");
    }if ($("#experience").hasClass("is-active")) {
      $("#experience").removeClass("is-active");
    }if ($("#contact").hasClass("is-active")) {
      $("#contact").removeClass("is-active");
    }
    $("#experience").addClass("is-active");
  });

  $("#contactbutton").on("click", function() {
    if ($("#about").hasClass("is-active")) {
    $("#about").removeClass("is-active");
  }if ($("#experience").hasClass("is-active")) {
    $("#experience").removeClass("is-active");
  }if ($("#contact").hasClass("is-active")) {
    $("#contact").removeClass("is-active");
  }
  $("#contact").addClass("is-active");
});

  $("#contactbutton1").on("click", function() {
      if ($("#about1").hasClass("is-active")) {
      $("#about1").removeClass("is-active");
    }if ($("#experience1").hasClass("is-active")) {
      $("#experience1").removeClass("is-active");
    }if ($("#contact1").hasClass("is-active")) {
      $("#contact1").removeClass("is-active");
    }
    $("#contact1").addClass("is-active");
  });

  $("#aboutbutton1").on("click", function() {
    if ($("#about1").hasClass("is-active")) {
    $("#about1").removeClass("is-active");
  }if ($("#experience1").hasClass("is-active")) {
    $("#experience1").removeClass("is-active");
  }if ($("#contact1").hasClass("is-active")) {
    $("#contact1").removeClass("is-active");
  }
  $("#about1").addClass("is-active");
});

$("#experiencebutton1").on("click", function() {
    console.log("Clicked");
    if ($("#about1").hasClass("is-active")) {
    $("#about1").removeClass("is-active");
  }if ($("#experience1").hasClass("is-active")) {
    $("#experience1").removeClass("is-active");
  }if ($("#contact1").hasClass("is-active")) {
    $("#contact1").removeClass("is-active");
  }
  $("#experience1").addClass("is-active");
});


  });
  
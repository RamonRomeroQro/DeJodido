(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();


  }); // end of document ready
})(jQuery); // end of jQuery name space


var nav = null;
    function requestPosition() {
        if (nav == null) {
            nav = window.navigator;
        }
        var geoloc = nav.geolocation;
        if (geoloc != null) {
            geoloc.getCurrentPosition(successCallback, errorCallback);
        }
    }
    function successCallback(position) {
        document.getElementById("latitude").value =
            position.coords.latitude;
        document.getElementById("longitude").value =
            position.coords.longitude;
    }
    function errorCallback(error) {
        var strMessage = "";
        // Check for known errors
        switch (error.code) {
            case error.PERMISSION_DENIED:
                strMessage = "Access to your location is turned off. "  +
                    "Change your settings to turn it back on.";
                break;
            case error.POSITION_UNAVAILABLE:
                strMessage = "Data from location services is " +
                    "currently unavailable.";
                break;
            case error.TIMEOUT:
                strMessage = "Location could not be determined " +
                    "within a specified timeout period.";
                break;
            default:
                break;
        }
        document.getElementById("status").innerHTML = strMessage;
    }

  // Or with jQuery


/// AQUI EL JQUERY AJAX PARA RECUPERAR LOS NOMBRES DE CIUDADES, CHECA: def listaciudades(request) en view.py

  $(document).ready(function(){
     $.ajax({
                url: '/ajax/get_ciudades/',
                data: {},
                dataType: 'json',
                success: function (data) {

                    $('input.autocomplete').autocomplete({
                      data : data
                    });

                }
              });
  });

    var nav = null;
    function requestPosition() {
        if (nav == null) {
            nav = window.navigator;
        }
        var geoloc = nav.geolocation;
        if (geoloc != null) {
            geoloc.getCurrentPosition(successCallback, errorCallback);
        }
    }
    function successCallback(position) {
        document.getElementById("latitude").value =
            position.coords.latitude;
        document.getElementById("longitude").value =
            position.coords.longitude;
    }
    function errorCallback(error) {
        var strMessage = "";
        // Check for known errors
        switch (error.code) {
            case error.PERMISSION_DENIED:
                strMessage = "Access to your location is turned off. "  +
                    "Change your settings to turn it back on.";
                break;
            case error.POSITION_UNAVAILABLE:
                strMessage = "Data from location services is " +
                    "currently unavailable.";
                break;
            case error.TIMEOUT:
                strMessage = "Location could not be determined " +
                    "within a specified timeout period.";
                break;
            default:
                break;
        }
        document.getElementById("status").innerHTML = strMessage;
    }
  // Or with jQuery
/// AQUI EL JQUERY AJAX PARA RECUPERAR LOS NOMBRES DE CIUDADES, CHECA: def listaciudades(request) en view.py
  $(document).ready(function(){
      $('select').formSelect();

      if (localStorage.getItem('jodido')){

      }else {
                localStorage.setItem('jodido', true);
                 $('#accessmodal').modal();
    $('#accessmodal').modal('open');// set


      }





     $.ajax({
                url: '/ajax/get_ciudades/',
                data: {},
                dataType: 'json',
                success: function (data) {
                    $('input.autocomplete').autocomplete({
                      data : data
                    });
                }
              });
  });



  $(document).ready(function(){
    $('.datepicker').datepicker();
  });





  // Or with jQuery

  $(document).ready(function(){
          $('.sidenav').sidenav();

    $('.slider').slider({    indicators:false,
    interva:1300,
    height:400, duration:500
    });

    //Agreagar a fucion scroll on load
    var clase=$('.stars');
    var i;
    for (i = 0; i < clase.length; i++) {
        var span = clase[i].id;
        var str=$("#"+span).html();
        var value= parseFloat(str);


        if (value<1) {
            $("#"+span).html('');
        } else if (value>=1 && value<1.7){
            $("#"+span).html('&#x2b50;');
        }else if (value>=1.7 && value<2.7){
            $("#"+span).html('&#x2b50;&#x2b50;');
        }else if (value>=2.7 && value<3.7){
            $("#"+span).html('&#x2b50;&#x2b50;&#x2b50;');
        }else if (value>=3.7 && value<4.7){
            $("#"+span).html('&#x2b50;&#x2b50;&#x2b50;&#x2b50;');
        }else if (value>=4.7 && value<=5){
            $("#"+span).html('&#x2b50;&#x2b50;&#x2b50;&#x2b50;&#x2b50;');
        }else {
            $("#"+span).html('Error');
        }










    }




  });
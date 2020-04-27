function degrees_to_radians(degrees)
{
  var pi = Math.PI;
  return degrees * (pi/180);
}

function radians_to_degrees(radians)
{
  var pi = Math.PI;
  return radians * (180/pi);
}



const R = 6378.1 ;
var est={
  center:{
    lat:20.592996,
    lon:-100.3918293,
  },
  pts:{
      0:{},
  60:{},
  120:{},
  180:{},
  240:{},
  300:{}
}

}

for(var p in est.pts) {
  //var value = est[key];
  firstEval=getCors(est.center.lat, est.center.lon, p)
  newLat = firstEval[0]
  newLon = firstEval[1]
  console.log(getCors(newLat, newLon, p+60))

  // do something with "key" and "value" variables

}

function getCors(lat_x,lon_x,degrees){

var brng = degrees_to_radians(degrees);
var d = 5 // Distance in km
var lat1 = degrees_to_radians(lat_x) //#Current lat point converted to radians
var lon1 = degrees_to_radians(lon_x) //#Current long point converted to radians

var lat2 = Math.asin( Math.sin(lat1)*Math.cos(d/R) +
     Math.cos(lat1)*Math.sin(d/R)*Math.cos(brng))

var lon2 = lon1 + Math.atan2(Math.sin(brng)*Math.sin(d/R)*Math.cos(lat1),
             Math.cos(d/R)-Math.sin(lat1)*Math.sin(lat2))

var lat2 = radians_to_degrees(lat2)
var lon2 = radians_to_degrees(lon2)
  // console.log(lat2)
  // console.log(lon2)
  return [lat2, lon2]
}



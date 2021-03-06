var map = L.map("map").setView([35, -99], 4.3);

// Add a tile layer
L.tileLayer('https://api.maptiler.com/maps/positron/{z}/{x}/{y}.png?key=G18kR4B5cKkYaH1F1cW3',
{attribution:'<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
}
).addTo(map)


var data = clinicalTrials[2];

for (var i = 0; i < data.length; ++i) {
  var popupContent = 
    '<br/><b>FACILITY:<b>   ' + data[i].facility +
    '<br/><b>Brief Title:<b>' + data[i].brieftitle +
    '<br/><b>Enrollment Count:</b> ' + data[i].enrollmentcount +
    '<br/><b>Contact Name:</b> ' + data[i].contactname +
    '<br/><b>Contact Phone:</b> ' + data[i].contactphone;

    var popupOptions =
    {
      'maxWidth': '500',
      'className': 'another-popup'
    }
  var m = L.marker([data[i].latitude, data[i].longitude], { icon: myIcon })
    .bindPopup(popupContent, popupOptions);

}















console.log("hot")

// listen for key responses
function map_update() {
    d3.select("#map_form").addEventListener("submit", function (e) {
        if (!isValid) {
            e.preventDefault();    //stop form from submitting (ignore)

            // getting all the checkmarks
            var x = document.getElementById("map_form");
            var i;
            var choice_array = "" //use string here, for easy conversion to query string
            for (i = 0; i < x.length; i++) {
                choice_array +=`,${x.element[i].value}`
            }
            console.log(choice_array)
        }
    }
    // d3.json("/results?").then(function (data) {
//     console.log(data[0])
//}
}

map_update();




// Function to determine states' color
function rankColor(state){

}

// Creating map object centered on US
var map = L.map("map", {
    center: [39.8283, -98.5795],
    zoom: 18
  });

// Adding mapbox tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 6,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(map);

// Our style object
var mapStyle = {
    color: "white",
    fillColor: rankColor, // reference function that gives color assignments based on percentile of range.
    fillOpacity: 0.5,
    weight: 1.5
  };

// Grabbing our GeoJSON data..
var state_outline_geoJSON ="https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json"

// need to add energy data to this GeoJSON.  
// build energy query using choice_array variable
var energy_query="?sources=&year="
d3.json()

d3.json(state_outline_geoJSON, function(data) {
    // Creating a GeoJSON layer with the retrieved data
    L.geoJson(data, {style:mapStyle}).addTo(map);
  });
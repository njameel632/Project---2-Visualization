

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

// Style object
var mapStyle = {
    color: "white",
    fillColor: rankColor, // reference function that gives color assignments based on percentile of range.
    fillOpacity: 0.5,
    weight: 1.5
  };

// Grabbing our GeoJSON data..
var state_outline_geoJSON ="https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json"
// Note: state_outline_geoJSON.features[i] gives state's data. Properties has info. 
var energy_JSON = d3.json("/results")

// Function to add state abbr.
function abbrState(input, to){
    
  var states = [
      ['Arizona', 'AZ'],
      ['Alabama', 'AL'],
      ['Alaska', 'AK'],
      ['Arkansas', 'AR'],
      ['California', 'CA'],
      ['Colorado', 'CO'],
      ['Connecticut', 'CT'],
      ['Delaware', 'DE'],
      ['Florida', 'FL'],
      ['Georgia', 'GA'],
      ['Hawaii', 'HI'],
      ['Idaho', 'ID'],
      ['Illinois', 'IL'],
      ['Indiana', 'IN'],
      ['Iowa', 'IA'],
      ['Kansas', 'KS'],
      ['Kentucky', 'KY'],
      ['Louisiana', 'LA'],
      ['Maine', 'ME'],
      ['Maryland', 'MD'],
      ['Massachusetts', 'MA'],
      ['Michigan', 'MI'],
      ['Minnesota', 'MN'],
      ['Mississippi', 'MS'],
      ['Missouri', 'MO'],
      ['Montana', 'MT'],
      ['Nebraska', 'NE'],
      ['Nevada', 'NV'],
      ['New Hampshire', 'NH'],
      ['New Jersey', 'NJ'],
      ['New Mexico', 'NM'],
      ['New York', 'NY'],
      ['North Carolina', 'NC'],
      ['North Dakota', 'ND'],
      ['Ohio', 'OH'],
      ['Oklahoma', 'OK'],
      ['Oregon', 'OR'],
      ['Pennsylvania', 'PA'],
      ['Rhode Island', 'RI'],
      ['South Carolina', 'SC'],
      ['South Dakota', 'SD'],
      ['Tennessee', 'TN'],
      ['Texas', 'TX'],
      ['Utah', 'UT'],
      ['Vermont', 'VT'],
      ['Virginia', 'VA'],
      ['Washington', 'WA'],
      ['West Virginia', 'WV'],
      ['Wisconsin', 'WI'],
      ['Wyoming', 'WY'],
  ];

  if (to == 'abbr'){
      input = input.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
      for(i = 0; i < states.length; i++){
          if(states[i][0] == input){
              return(states[i][1]);
          }
      }    
  } else if (to == 'name'){
      input = input.toUpperCase();
      for(i = 0; i < states.length; i++){
          if(states[i][1] == input){
              return(states[i][0]);
          }
      }    
  }
}

// Function to determine states' color
function rankColor(state){

}

// Append data from energy JSON to GeoJSON.  KEYS: features[0++] > properties + ENERGY>amount
d3.json(state_outline_geoJSON, function(data) {
  
  for (i=0; i < state_outline_geoJSON.features.length; i++) {
    var properties = state_outline_geoJSON.features[i].properties // sets variable for properties modification
    
    //add state abbreviation to properties
    properties.ABBR = abbrState(features[i].properties.STATE, 'abbr') 
    var abbr = properties.ABBR

    //add energy value to properties
    properties.ENERGY = energy_JSON.map[abbr]
  }

  // Creating a GeoJSON layer with the retrieved data
    L.geoJson(data, {style:mapStyle}).addTo(map);
  });
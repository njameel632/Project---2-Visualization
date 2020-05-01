console.log("hot")

function map_update() {
    d3.select("#map_form").addEventListener("submit", function (e) {
        if (!isValid) {
            e.preventDefault();    //stop form from submitting (ignore)
            
            // getting all the checkmarks
            var x = document.getElementById("map_form");
            var i;
            var choice_array = []
            for (i = 0; i < x.length; i++) {
                choice_array.push(x.element[i].value)
            }
            console.log(choice_array)
        }
    }
    // d3.json("/results?").then(function (data) {
//     console.log(data[0])
}

map_update();
function getLine() {
  d3.json("/results").then((importeddata) => {
    console.log(importeddata);

    var data = importeddata;

    // var filtereddata = data.linegraph.filter((y) => y.year_energy);

    var trace1 = {
      x: data.map((row) => row.Conventional_Energy),
      y: data.map((row) => row.year_energy),
      type: "line",
      //   mode: "lines",
    };

    var trace2 = {
      x: data.map((row) => row.year_energy),
      y: data.map((row) => row.Green_Energy),
      type: "line",
      //   mode: "lines",
    };

    var chartData = [trace1, trace2];

    var layout = {
      title: "Green VS Conventional Energy Over Time",
      margin: {
        l: 100,
        r: 100,
        t: 100,
        b: 100,
      },
    };

    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("plot1", chartData, layout);
  });
}

// Getting Bargraph Data

function getBar(bar) {
  d3.json("/results").then((response) => {
    console.log(response);

    bar_data = response["bargraph"];

    var trace3 = {
      x: bar_data.map((b) => b.state_id),
      y: bar_data.map((m) => m.megawatthours),
      type: "bar",
    };

    var charData1 = [trace3];

    var layout1 = {
      title: "Energy Production By State Per From 1990-2018",
      margin: {
        l: 100,
        r: 100,
        t: 100,
        b: 100,
      },
    };

    Plotly.newPlot("plot", charData1, layout1);
  });
}

getLine();

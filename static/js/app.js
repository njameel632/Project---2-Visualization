d3.json("results.json").then(function (data) {
  console.log(data);

  var bargraph = data.bargraph;

  var trace1 = {
    x: bargraph.map((row) => row.year_energy),
    y: bargraph.map((row) => row.Conventional_Energy),
    text: bargraph.map((row) => row.Conventional_Energy),
    name: "Energy",
    type: "bar",
    orientation: "h",
  };

  var trace2 = {
    x: bargraph.map((row) => row.year_energy),
    y: bargraph.map((row) => row.Green_Energy),
    type: "bar",
    orientation: "h",
  };

  // Apply the group bar mode to the layout
  var layout = {
    title: "Energy Comparison",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100,
    },
  };

  var chartdata = [trace1, trace2];

  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("bar_graph", chartdata, layout);
});

//  Line Graph

d3.json("results.json").then(function (data1) {
  console.log(data1);

  var linegraph = data1.linegraph;

  var trace3 = {
    x: linegraph.map((c) => c.year_energy),
    y: linegraph.map((c) => c.Conventional_Energy),
    type: "scatter",
    mode: "lines",
  };

  var trace4 = {
    x: linegraph.map((c) => c.year_energy),
    y: linegraph.map((c) => c.Green_Energy),
    type: "scatter",
    mode: "lines",
  };

  var layout1 = {
    title: "Line Graph For Energy Production Over Time 1990-2018",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100,
    },
  };

  var chartdata1 = [trace3, trace4];

  Plotly.newPlot("line_graph", chartdata1, layout1);
});

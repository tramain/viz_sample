d3js.org/d3.v3.min.js
// ring format
var data = [{% for d in dataValue %}
  {{d}},
  {% endfor %}];

// var name = [{% for v in dataType %}
//   {{v}},
//   {% endfor %}];

var width = 960,
    height = 500,
    radius = height / 2 - 10;

var arc = d3.svg.arc()
    .innerRadius(radius - 40)
    .outerRadius(radius);

var pie = d3.layout.pie()
    .padAngle(.02);

var color = d3.scale.category10();

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

svg.selectAll("path")
    .data(pie(data))
  .enter().append("path")
    .style("fill", function(d, i) { return color(i); })
    .attr("d", arc);

// svg.append("text")
//     .attr("class", "title")
//     .attr("x", x(data[0].name))
//     .attr("y", -26)
//     .text("Why Are We Leaving Facebook?");

// svg.append("text")
//     .data(pie(name))
//   .enter().append("path")
//     .style("fill", function(d, i) { return color(i); })
//     .attr("d", arc);

// function type(d) {
//   d.value = +d.value; // coerce to number
//   return d;
// }


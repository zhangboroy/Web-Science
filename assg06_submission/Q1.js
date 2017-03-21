.links line {
  stroke: #999;
  stroke-opacity: 0.6;
}
 
.nodes circle {
  stroke: #fff;
  stroke-width: 1.5px;
}

var w=960,h=500;
var svg=d3.select("#chart")
    .append("svg")
    .attr("width",w).attr("height",h);

d3.json("graph.json", function(error, graph) {
    var simulation = d3.forceSimulation()
      .nodes(graph.nodes);

    var node = svg.append("g")
      .attr("class", "nodes")
      .selectAll("circle")
      .data(nodes_data)
      .enter()
      .append("circle")
      .attr("r", 5)
      .attr("fill", "red");

    var link_force =  d3.forceLink(graph.links)
      .id(function(d) { return d.username; })

    simulation.force("links",link_force)

    var link = svg.append("g")
      .attr("class", "links")
      .selectAll("line")
      .data(graph.links)
      .enter().append("line")
      .attr("stroke-width", 2);
});
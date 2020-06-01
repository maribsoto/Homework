// The code for the chart is wrapped inside a function
// that automatically resizes the chart
function makeResponsive() {

  // Store width and height parameters
  var svgWidth = 960;
  var svgHeight = 500;

  // Set up margins
  var margin = {
    top: 20,
    right: 40,
    bottom: 60,
    left: 100
  };

  // Create width and height parameters based on SVG margins (left and right)

  var width = svgWidth - margin.left - margin.right;
  var height = svgHeight - margin.top - margin.bottom;

  // Create an SVG wrapper, append an SVG group that holds the chart
  // and shift the latter by left and top margins.
  var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

  var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

  // Import Data
  var file = "assets/data/data.csv"

  d3.csv(file).then(successHandler, errorHandler);

  function errorHandler(error) {
    throw err;
  }

  function successHandler(healthData) {
    // Step 1: Parse Data/Cast as numbers
    // ==============================
    healthData.forEach(function (data) {
      data.age = +data.age;
      data.smokes = +data.smokes;
      data.healthcare = +data.healthcare;
      data.poverty = +data.poverty;
      data.abbr = data.abbr;
      data.income = +data.income;
      data.state = data.state;
    });

    // Step 2: Create scale functions
    // ==============================
    var xLinearScale = d3.scaleLinear()
      .domain([8.5, d3.max(healthData, d => d.poverty)])
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([3.5, d3.max(healthData, d => d.healthcare)])
      .range([height, 0]);

    // Step 3: Create axis functions
    // ==============================python -m http.server 8000 --bind 127.0.0.1
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Step 4: Append Axes to the chart
    // ==============================
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    var toolTip = d3
      .tip()
      .attr("class", "d3-tip")
      .offset([40, -60])
      .html(function (d) {

        var theX;

        var theState = "<div>" + d.state + "</div>";

        var theY = "<div>" + curY + ": " + d[curY] + "%</div>";

        if (curX === "poverty") {

          theX = "<div>" + curX + ": " + d[curX] + "%</div>";
        }
        else {

          theX = "<div>" +
            curX +
            ": " +
            parseFloat(d[curX]).toLocaleString("en") +
            "</div>";
        }

        return theState + theX + theY;
      });

    svg.call(toolTip);
    // Step 5: Create Circles for scatter plot
    // =======================================
    var circlesGroup = chartGroup.selectAll("circle")
      .data(healthData)
      .enter()
      .append("circle")
      .attr("cx", d => xLinearScale(d.poverty))
      .attr("cy", d => yLinearScale(d.healthcare))
      .attr("r", "13")
      .attr("fill", "blue")
      .attr("opacity", ".4")
     
    // Append text to circles

    chartGroup.select("g")
      .selectAll("circle")
      .data(healthData)
      .enter()
      .append("text")
      .attr("x", d => xLinearScale(d.poverty))
      .attr("y", d => yLinearScale(d.healthcare))
      .attr("dy", -415)
      .attr("text-anchor", "middle")
      .attr("font-size", "10px")
      .attr("fill", "black")
      .text(d => (d.abbr))
      .on("mouseover", function (d) {
        toolTip.show(d, this);

        d3.select(this).style("stroke", "#323232");
      })
      .on("mouseout", function (d) {

        toolTip.hide(d);

        d3.select(this).style("stroke", "#e3e3e3");
      });

    // Step 6: Initialize tool tip
    //==============================


    // Create axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Lacks Healthcare (%)");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("In Poverty (%)");
  }
}

// When the browser loads, makeResponsive() is called.
makeResponsive();

// When the browser window is resized, responsify() is called.
d3.select(window).on("resize", makeResponsive);
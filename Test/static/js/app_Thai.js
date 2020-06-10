function metadata() {

  var url = "/api/v1.0/metadata";

  d3.json(url).then(function(data) {
    
    d3.select("tbody")
      .selectAll("tr")
      .data(data)
      .enter()
      .append("tr")
      .html(function(d) {
        return `<td>${d.Name}</td><td>${d.Status}</td><td>${d.Birth_Date}</td><td>${d.Undergraduate_Major}</td><td>${d.Graduate_Major}</td><td>${d.Military_Rank}</td><td>${d.Mission_One}</td><td>${d.Mission_Two}</td><td>${d.Mission_Three}</td><td>${d.Mission_Four}</td>`
      });
});

}

var filters = {};

function updateFilters() {

  var changedElement = d3.select(this).select("input");
  var elementValue = changedElement.property("value");
  var filterId = changedElement.attr("id");

  if (elementValue) {
    filters[filterId] = elementValue;
  }
  else {
    delete filters[filterId];
  }

  filterTable();
}

function filterTable() {

  var url = "/api/v1.0/metadata";

  d3.json(url).then(function(data) {

    var filteredData = data;

    Object.entries(filters).forEach(([key, value]) => {
      filteredData = filteredData.filter(row => row[key] === value);
    });
  });

  d3.select("tbody")
      .selectAll("tr")
      .data(filteredData)
      .enter()
      .append("tr")
      .html(function(d) {
        return `<td>${d.Name}</td><td>${d.Status}</td><td>${d.Birth_Date}</td><td>${d.Undergraduate_Major}</td><td>${d.Graduate_Major}</td><td>${d.Military_Rank}</td><td>${d.Mission_One}</td><td>${d.Mission_Two}</td><td>${d.Mission_Three}</td><td>${d.Mission_Four}</td>`
      });

}

d3.select("#filter-btn").on("click", filterTable);

metadata();







// from data.js
// Get a reference to the following variables
var url = "/api/v1.0/metadata";

// Fetch the JSON data and console log it
d3.json(url).then(SuccesHandler);

function metadata(dataInput) {
  // Step 1: Parse Data/Cast as numbers
  // ==============================
  dataInput.forEach(function (data) {
    data.Name = data.Name;
    data.Status = data.Status;
    data.Birth_Date = +data.Birth_Date;
    data.Undergraduate_Major = data.Undergraduate_Major;
    data.Graduate_Major = data.Graduate_Major;
    data.Military_Rank = data.Military_Rank;
    data.Mission_One = data.Mission_One;
  });
}
var tbody = d3.select("tbody");
var inputFieldName = d3.append("#name");
var inputFieldStatus = d3.append("#status");
var inputFieldBirth = d3.append("#birth");
var inputFieldUnd = d3.select("#und");
var columns = ["name", "status", "birth", "und"]

// Appending a table to the webpage, adding rows and the given columns
var populate = (dataInput) => {

  dataInput.forEach(NasaTable => {
    var row = tbody.append("tr");
    columns.forEach(column => row.append("td").text(NasaTable[column])
    )
  });
}
// Populating the table
populate(data);

// Console.log the ufo data from data.js
console.log(data)

// Filters attributes and creating a button for this
// Defining our Filter button
var button = document.getElementById("filter-btn")

button.addEventListener("click", function (e) {
  e.preventDefault()
  console.log('It Works')
  // Defining input variables
  var inputName = inputFieldName.property("value").trim();
  var inputStatus = inputFieldStatus.property("value").toLowerCase().trim();
  var inputBirth = inputFieldBirth.property("value").trim();
  var inputUnd = inputFieldUnd.property("value").toLowerCase().trim();

  // Filters by field matching input value
  var filterName = data.filter(data => data.Name === inputName);
  var filterStatus = data.filter(data => data.Status === inputStatus);
  var filterBirth = data.filter(data => data.Birth_Date === inputBirth);
  var filterUnd = data.filter(data => data.Undergraduate_Major === inputUnd);
  var filterData = data.filter(data => data.Name === inputName && data.Status === inputStatus);

  // Adding the requested all filters to table
  tbody.html("");

  let response = {
    filterData, filterName, filterStatus, filterBirth, filterUnd
  }

  if (response.filterData.length !== 0) {
    populate(filterData);
  }

  if (response.filterName.length !== 0) {
    populate(filterName);
  }

  if (response.filterStatus.length !== 0) {
    populate(filterStatus);
  }
  else if (response.filterData.length === 0 && ((response.filterName.length !== 0 || response.filterStatus.length !== 0))) {
    populate(filterName) || populate(filterStatus);
  }
  // If the date filter does not work, then:
  else {
    tbody.append("tr").append("td").text("Unfortunately No Astronauts Facts... Let's move on!");
  }
})

// Adding a Reset button
const reset_button = document.getElementById("reset-btn")
reset_button.addEventListener("click", function (e) {
  e.preventDefault()
  console.log('Reset Works')
  tbody.html("");
  populate(data)

})
function getBalconyValue() {
  var uiBalcony = document.getElementsByName("uiBalcony");
  for (var i = 0; i < uiBalcony.length; i++) {
    if (uiBalcony[i].checked) {
      return parseInt(uiBalcony[i].value);
    }
  }
  return -1; // Invalid Value
}

function getNo_of_roomsValue() {
  var uiNo_of_rooms = document.getElementsByName("uiNo_of_rooms");
  for (var i = 0; i < uiNo_of_rooms.length; i++) {
    if (uiNo_of_rooms[i].checked) {
      return parseInt(uiNo_of_rooms[i].value);
    }
  }
  return -1; // Invalid Value
}

function getNewly_constructed() {
  var uiNewly_constructed = document.getElementsByName("uiNewly_constructed");
  for (var i = 0; i < uiNewly_constructed.length; i++) {
    if (uiNewly_constructed[i].checked) {
      return parseInt(uiNewly_constructed[i].value);
    }
  }
  return -1; // Invalid Value
}

function getKitchen() {
  var uiKitchen = document.getElementsByName("uiKitchen");
  for (var i = 0; i < uiKitchen.length; i++) {
    if (uiKitchen[i].checked) {
      return parseInt(uiKitchen[i].value);
    }
  }
  return -1; // Invalid Value
}

function getCellar() {
  var uiCellar = document.getElementsByName("uiCellar");
  for (var i = 0; i < uiCellar.length; i++) {
    if (uiCellar[i].checked) {
      return parseInt(uiCellar[i].value);
    }
  }
  return -1; // Invalid Value
}

function getLift() {
  var uiLift = document.getElementsByName("uiLift");
  for (var i = 0; i < uiLift.length; i++) {
    if (uiLift[i].checked) {
      return parseInt(uiLift[i].value);
    }
  }
  return -1; // Invalid Value
}

function getGarden() {
  var uiGarden = document.getElementsByName("uiGarden");
  for (var i = 0; i < uiGarden.length; i++) {
    if (uiGarden[i].checked) {
      return parseInt(uiGarden[i].value);
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimateRent() {
  console.log("Estimate Rent button clicked");
  var sqm = document.getElementById("uiSqm");
  var Balcony = getBalconyValue();
  var No_of_rooms = getNo_of_roomsValue();
  var Newly_constructed = getNewly_constructed();
  var Kitchen = getKitchen();
  var Cellar = getCellar();
  var Lift = getLift();
  var Garden = getGarden();
  var floor = document.getElementById("uifloor");
  var location = document.getElementById("uiLocations");
  var estRent = document.getElementById("uiEstimatedRent");

  var url = "http://127.0.0.1:5000/predict_rent"; //Use this if you are NOT using nginx 
  //var url = "/api/predict_rent"; // Use this if you are using nginx.

  $.post(url, {
      living_space: parseFloat(sqm.value),
      balcony: Balcony,
      no_of_rooms: No_of_rooms,
      newly_constructed: Newly_constructed,
      has_kitchen: Kitchen,
      cellar: Cellar,
      lift: Lift,
      garden: Garden,
      floor: floor.value,
      location: location.value
  }, function(data, status) {
      console.log("Response data:", data);
      if (data.estimated_rent) {
          estRent.innerHTML = "<h2>" + data.estimated_rent.toString() + " EUROS</h2>";
      } else {
          estRent.innerHTML = "<h2>Unable to estimate rent. Please try again later.</h2>";
          console.error("Estimated rent is undefined");
      }
      console.log(status);
  }).fail(function(xhr, status, error) {
      console.error("Error: " + error);
      estRent.innerHTML = "<h2>Unable to estimate rent. Please try again later.</h2>";
  });
}

function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_location_name"; 
  //var url = "/api/get_location_name"; 
  var floorUrl = "http://127.0.0.1:5000/get_floor_name";
  //var floorUrl = "/api/get_floor_name";
  $.get(url, function(data, status) {
      console.log("got response for get_location_names request");
      if (data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for (var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
  $.get(floorUrl, function(data, status) {
      console.log("got response for get_floor_name request");
      console.log("Response data:", data);
      if (data) {
          var floors = data.floors;
          var uifloor = document.getElementById("uifloor");
          $('#uifloor').empty();
          for (var i in floors) {
              var opt = new Option(floors[i]);
              $('#uifloor').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;

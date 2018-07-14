let mymap = L.map('mapid').setView([52.5247258, 13.3930329], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiamFob25naXJyIiwiYSI6ImNqamJndXp6bTBoMWszcXFrczZtMDQ3YWgifQ.xe7WnnoPTFfegmrvIumsRw'
}).addTo(mymap);

function onEachFeature(feature, layer) {
  let marker = L.marker(feature.properties.location.coordinates).addTo(mymap);
  marker.bindPopup(feature.properties.name).openPopup();
}

$.get("/restaurants/").done(function (data) {
  L.geoJson(data, {
    onEachFeature: onEachFeature
  }).addTo(mymap)
}).fail(function () {
  alert("Error while getting restaurants");
});

$("#optimize-btn").click(function () {
  let btnText = $(this).text();
  $(this).html("Loading...");

  $.post("/restaurants/optimize/")
    .done(function () {
      location.reload();
    }).fail(function () {
      alert("Error while optimizing");
    }).always(function () {
      $("#optimize-btn").text(btnText);
    });
});

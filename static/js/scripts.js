var mymap = L.map('map').setView([55.8,37.5], 12);


	var MapBoox = L.tileLayer('https://api.mapbox.com/styles/v1/kraipen/ckhg857ua17xl19md3hrzenql/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoia3JhaXBlbiIsImEiOiJja2hnNzg0Y3YwZnBkMnJxcWJuNXp5Nnk0In0.lM3_csSiXV9DfS5XSg4tMA', {
     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    });

	var googletiles = L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
	attribution: 'Google'
	});
	var OSMtiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(mymap);


	var baseMaps = {
	"Google": googletiles,
	"OSM": OSMtiles,
	"Map":MapBoox,
	};
var Controller = L.control.layers(baseMaps, overlayMaps).addTo(mymap);

var marker = L.marker([55.8, 37.5]).addTo(mymap);

marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();

//var popup = L.popup()
//    .setLatLng([55.8,37.5])
//    .setContent("I am a standalone popup.")
//    .openOn(mymap);


//	 var overlayMaps = { };
//var mymap = L.map('map').setView([40.179,-101.733], 5);
//
//
//	var MapBoox = L.tileLayer('https://api.mapbox.com/styles/v1/kraipen/ckhg857ua17xl19md3hrzenql/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoia3JhaXBlbiIsImEiOiJja2hnNzg0Y3YwZnBkMnJxcWJuNXp5Nnk0In0.lM3_csSiXV9DfS5XSg4tMA', {
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//    });
//
//	var googletiles = L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
//	attribution: 'Google'
//	});
//	var OSMtiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
//	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
//	}).addTo(mymap);


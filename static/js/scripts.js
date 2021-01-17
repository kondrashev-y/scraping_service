var mymap = L.map('map').setView([55.8,37.5], 12);


//	var MapBoox = L.tileLayer('https://api.mapbox.com/styles/v1/kraipen/ckhg857ua17xl19md3hrzenql/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoia3JhaXBlbiIsImEiOiJja2hnNzg0Y3YwZnBkMnJxcWJuNXp5Nnk0In0.lM3_csSiXV9DfS5XSg4tMA', {
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//    });

	var googletiles = L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
	attribution: 'Google'
	}).addTo(mymap);

	var OSMtiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	});



	var baseMaps = {
	"Google": googletiles,
	"OSM": OSMtiles,
	};
var Controller = L.control.layers(baseMaps, overlayMaps).addTo(mymap);

//var marker = L.marker([55.8, 37.5]).addTo(mymap);
//var marker_v = L.marker([55.82, 37.52]).addTo(mymap);

let fruits = [[55.8, 37.5], [55.84, 37.54], [55.82, 37.52]];

for (let fruit of fruits) {
  var marker = L.marker(fruit).addTo(mymap);
  marker.bindPopup("<b>Hello world!</b><br>I am a popup");
}


//marker.bindPopup("<b>Hello world!</b><br>I am a popup");
//marker_v.bindPopup("<b>Hello world!</b><br>I am a popup<a href='http://127.0.0.1:2000/'>my app</a> ");



	 var overlayMaps = { };
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


//var countyData = JSON.parse(document.getElementById('my_dictionary-data').textContent);
//alert(countyData);

//var my_data = JSON.parse(document.getElementById('my_dictionary').textContent);
var my_data = JSON.parse(document.getElementById('my_dictionary').innerHTML);
my_data = JSON.parse(my_data);
//var my_data = JSON.parse(document.getElementById('my_dictionary').textContent, function(k, v) {
//  console.log(k); // пишем имя текущего свойства, последним именем будет ""
//  return v;       // возвращаем неизменённое значение свойства
//});
//var my_data = JSON.parse(document.getElementById('my_dictionary').innerHTML);
//var my_data = document.getElementById('my_dictionary').innerHTML;

for (key in my_data) {
  if (my_data.hasOwnProperty(key)) {
    //ключ = key
    //значение = person[key]
    console.log("Ключ = " + key);
    console.log("Значение = " + my_data[key]);
  }
}
//
//
//for (var i=0; i<=my_data.moscow.length-1; i++) {
//  if (my_data.moscow[i].hasOwnProperty(key)) {
//    console.log("Элемент [ "+ i +" ] = " + my_data.moscow[i]);
//  }


//var user_list = [];
//
//$.each( my_data, function( key, value ) {
//    user_list.push( value );
//});
//
//alert(typeof user_list);


//for (let data of my_data) {
//alert(data);
//}

alert(typeof my_data);
alert(my_data);


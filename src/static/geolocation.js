function geoFindMe() {
	var output = document.getElementById("out");
	//var html_lon = document.getElementById("lon");
	//var html_lat = document.getElementById("lat");

	if (!navigator.geolocation){
		output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
		return;
	}

	function success(position) {
		var latitude  = position.coords.latitude;
		var longitude = position.coords.longitude;
		//output.innerHTML = '<p>Latitude is ' + latitude + '° <br>Longitude is ' + longitude + '°</p>';
		document.getElementById("lon").value = Number(longitude);
		document.getElementById("lat").value = Number(latitude);
		output.innerHTML = "<p>Location Stored!</p>";
	}

	function error() {
		output.innerHTML = "<p>Unable to retrieve your location</p>";
	}

	output.innerHTML = "<p>Locating…</p>";

	navigator.geolocation.getCurrentPosition(success, error);
}
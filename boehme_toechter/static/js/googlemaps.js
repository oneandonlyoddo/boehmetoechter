function initialize() {
	var map_canvas = document.getElementById('map_div');
	var myLatLng = new google.maps.LatLng(51.256753,11.721843);

	var map_options = {
		center: myLatLng,
		zoom: 9,
		mapTypeId: google.maps.MapTypeId.ROADMAP

	}
	
	var map = new google.maps.Map(map_canvas, map_options)
	var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
	var marker = new google.maps.Marker({
		position: myLatLng,
		map: map
	});
}

google.maps.event.addDomListener(window, 'load', initialize);


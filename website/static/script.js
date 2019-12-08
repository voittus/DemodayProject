function initMap() {
    // The location of Uluru
    var sp = { lat: -23.5489, lng: -46.6388 };
    // The map, centered at sp
    var map = new google.maps.Map(
        document.getElementById('map'), { zoom: 11, center: sp });
    // The marker, positioned at sp
    var markers = new google.maps.Marker(
        {
            position: new google.maps.LatLng(-23.5356, -46.5272),
            map: map
        },

    );
    var markers = new google.maps.Marker({
        position: new google.maps.LatLng(-23.5271, -46.6593),
        map: map
    })
}
initMap();




var nav = responsiveNav("#nav-collapse");


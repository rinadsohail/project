var map;
    var service;
    var infowindow;
    var locationList = document.getElementById('location-list');

    function initialize() {
      var pyrmont = new google.maps.LatLng(51.505, -0.09); // Coordinates of London

      map = new google.maps.Map(document.getElementById('map'), {
        center: pyrmont,
        zoom: 15
      });

      var input = document.getElementById('pac-input');
      var searchBox = new google.maps.places.SearchBox(input);
      map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

      searchBox.addListener('places_changed', function () {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
          return;
        }

        // Clear previous search results
        locationList.innerHTML = '';

        var bounds = new google.maps.LatLngBounds();
        places.forEach(function (place) {
          if (!place.geometry) {
            console.log("Returned place contains no geometry");
            return;
          }

          if (place.geometry.viewport) {
            bounds.union(place.geometry.viewport);
          } else {
            bounds.extend(place.geometry.location);
          }

          // Display each place in the list
          displayPlace(place);
        });
        map.fitBounds(bounds);
      });

      infowindow = new google.maps.InfoWindow();
      service = new google.maps.places.PlacesService(map);
    }

    function displayPlace(place) {
      var listItem = document.createElement('div');
      listItem.classList.add('location-item');
      listItem.innerHTML = '<strong>' + place.name + '</strong><br>' + place.formatted_address;
      locationList.appendChild(listItem);
    }

    initialize();
3
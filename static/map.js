"use strict";
function initMap() {
    const sf = {
        lat: 37.773972,
        lng: -122.431297
    };

    const basicMap = new google.maps.Map(
        document.querySelector('#map'),
        {
            center: sf,
            zoom: 11
        }
    );


    // test San Francisco marker
    const sfMarker = new google.maps.Marker({
        position: sf,
        title: 'SF',
        map: basicMap
    });


    const sfInfo = new google.maps.InfoWindow({
        content: '<h5>This is one of the best cities in the World!</h5>'
    });

    // test San Francisco marker event listener
    sfMarker.addListener('click', () => {
        sfInfo.open(basicMap, sfMarker);
    });




    const schoolAddresses = [];
    $('.dance_school').each((i, linkElement) => {
        schoolAddresses.push({
            address: $(linkElement).data('address'),
            name: $(linkElement).data('name'),
          });
        
    });


    const geocoder = new google.maps.Geocoder();
    for (const addrSchool of schoolAddresses) {
        geocoder.geocode(
            { address: addrSchool['address'] },
            (results, status) => {
                if (status === 'OK') {
                    const schoolLocation = results[0].geometry.location;

                    const schoolLocationMarker = new google.maps.Marker({
                        position: schoolLocation,
                        map: basicMap
                    });

                    const schoolInfo = new google.maps.InfoWindow({
                        content: '<h5>School: '+addrSchool['name']+' <br>Address: '+addrSchool['address']+'</h5>'
                    });

                    schoolLocationMarker.addListener('click', () => {
                        schoolInfo.open(basicMap, schoolLocationMarker);
                    });

                }

            });
    }

}

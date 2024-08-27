$(document).ready( function () {
    $.ajax('https://swapi-api.alx-tools.com/api/films/?format=json')
        .done( function (json) {
            $.each(json.results, function (index, value) {
                $('<li>' + value.title + '</li>').appendTo( $('UL#list_movies') );
            });
        });
});
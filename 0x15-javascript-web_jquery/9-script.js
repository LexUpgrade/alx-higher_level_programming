$(document).ready( function () {
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        dataType: 'json',
    })
        .done( function (json) {
            $('DIV#hello').html(json.hello);
        })
});
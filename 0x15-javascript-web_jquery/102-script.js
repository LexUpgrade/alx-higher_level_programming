$(document).ready( function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $('INPUT#btn_translate').click( function () {
        $.get ( url + $.param({ lang: $('INPUT#language_code')}), function (json) {
           $('DIV#hello').html(json.hello);
        });
    });
});
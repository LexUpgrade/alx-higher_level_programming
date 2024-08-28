$(document).ready( function () {
    $('INPUT#btn_translate').click(translator);
    $('INPUT#btn_transalte').focus( function () {
        $(this).keydown( function (key) {
            if ( key === '13' ) {
                translator();
            }
        });
    });
});

function translator() {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (json) {
        $('DIV#hello').html(json.hello);
    });
}
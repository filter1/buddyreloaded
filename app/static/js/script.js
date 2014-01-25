$(document).ready(function() {

    $('#train').hide();

    $('#radio_pre').click(function() {
       $('#train').show();
    });

    $('#radio_inc').click(function() {
       $('#train').hide();
    });
});
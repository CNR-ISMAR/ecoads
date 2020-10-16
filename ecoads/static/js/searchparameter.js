$(document).ready(function(){
    $("#parameter-search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#parameter-list div").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    });
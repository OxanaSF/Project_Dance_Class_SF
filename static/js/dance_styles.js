$(document).ready(function() {
    $('.search-filter').select2();
});

$(document).ready(function(){
    $(".search-filter").change(function(){

        var selectedCOption = $(this).children("option:selected").val();
       
        $('#search-submit').click(function(){
            window.location.href='/dance_style/'+selectedCOption;
        });
});
});


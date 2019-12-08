// Select2 search script
$(document).ready(function() {
    $('.search-filter').select2();
});

$(document).ready(function(){
    $(".search-filter").change(function(){

        var selectedCOption = $(this).children("option:selected").val();
       
        // $('#search-submit').click(function(){
            window.location.href='/dance_teachers/'+selectedCOption;
        // });
});
});




// Modal script for adding new teacher
$(document).ready(() => {
    $('#add_teacher').click(function(){
    // setTimeout(() => {
        $('#modal_add_form').modal('show');
        
        // setTimeout (() => {
        //     $('#modal_add_form').modal('hide')
        // }, 10000);
    }, 3000);
});


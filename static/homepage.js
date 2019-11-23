
// render the homepage to the search page after clicking on the search button
//$('#search-btn').click(function(){
    // 1. Get the search term from form
    //maybe for drop down button I need to change val - check it
    //var dance_style = $("#search_field_dance_style")//.val();

    // 2. Put value into 
    //window.location.href='/search?classes=' + dance_style;
 //})

// 1
// $('#search-btn').click(function(){
//     window.location.href='/dance_styles'
// })


$(document).ready(function(){
    $("select.option_btw_style_school").change(function(){
        var selectedCOption = $(this).children("option:selected").val();
        $("#search-btn").click(function(){
            
        if(selectedCOption == 'Dance style'){
            window.location.href='/dance_styles'
            // alert("You have selected - " + 'Dance style');

        } else if (selectedCOption == 'Dance teacher') {
            window.location.href='/dance_teachers'
        
        }else{
            window.location.href='/dance_schools'
            // alert("You have selected - " + 'Dance school');
        }
    });
});
});



// 3
//  $('#register').click(function(){
//     window.location.href='/register';
//  })

 $(document).ready(function(){
    var arrow = $(".arrow-up");
    var form= $(".login-form");
    var status = false;
        $("#login").mouseover(function(event){
            event.preventDefault();
            if(status == false){
                arrow.fadeIn();
                form.fadeIn();
                status = true;
            }else{
                arrow.fadeOut();
                form.fadeOut();
                status = false;
            }

        })
    
 })





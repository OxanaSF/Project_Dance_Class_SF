$(document).ready(function(){
    
$("#search-btn").click(function(){

    var selectedCOption = $("select.option_btw_style_school").children("option:selected").val();
        
            
    if(selectedCOption == 'Dance styles'){
        window.location.href='/dance_styles';
        // alert("You have selected - " + 'Dance style');

    } else if (selectedCOption == 'Dance teachers') {
        window.location.href='/dance_teachers';
    
    }else{
        window.location.href='/dance_schools'
        // alert("You have selected - " + 'Dance school');
    }
});

});

 $(document).ready(function(){
    var arrow = $(".arrow-up-left");
    var form= $(".login-form");
    var status = false;
        $("#login").click(function(event){
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


 $(document).ready(function(){
    var arrow = $(".arrow-up-right");
    var form= $(".register-form-right");
    var status = false;
        $("#register").click(function(event){
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





$('#search-btn').click(function(){
    window.location.href='/register';
 })

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


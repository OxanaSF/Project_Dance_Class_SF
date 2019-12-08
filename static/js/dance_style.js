$('.choose_style').on('change', function(){
    var dance_style = $(this).val();
    alert(dance_style);

    // 2. Put value into 
    window.location.href='/search?style='+ dance_style;
 })
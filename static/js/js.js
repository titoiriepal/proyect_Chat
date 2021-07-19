window.onload = function() 
{


    $.ajax({
        url: "/ajax",
        type: "post",
        data: null,
        dataType: 'json',
        success: function(data){
            console.log(data);
            console.log(data.id);   
        }
    });


}

jQuery.noConflict();
// jQuery(document).ready(functions($)
// {
//     $("#btn-1").click(function()
//     {
//         alert('clicked');
//         // $("#image").fadeOut(function(){});)
//     });
// });

jQuery(document).ready(function($)
{
    $("#image").hover(function()
    {
        $("#image").addClass("img-thumbnail");
        // $("#image").hide(1000,function(){});
    },function () { 
        // $(this).show(1000,function(){});
        $("#image").removeClass("img-thumbnail");
     });
});
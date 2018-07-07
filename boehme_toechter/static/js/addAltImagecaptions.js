function AddImageAltCaption(){
    // display image caption on top of image
$('.plugin_picture img').each(function() {
var imageCaption = $(this).attr("alt");
 
$(this).closest(".plugin_picture").append("<p class='bildunterschrift'>"+imageCaption+"</p>");

});
 
}


 
 
$(document).ready(AddImageAltCaption);
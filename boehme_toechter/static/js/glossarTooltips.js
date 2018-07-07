
function findTerms() {
 $(function () 
 {
  $.ajax({                                      
    url: 'http://boehme-toechter.sites.djangoeurope.com/api.php',       
    data: "",                        
    dataType: 'json',                
    success: function(rows)          
    {
      for (var i in rows)
      {
        var row = rows[i];          
        var dbterm = rows[i]['term'];
        var description = rows[i]['description'];
               
        $("span:contains('" + dbterm + "')").replaceWith(function() {
      
          var term = $.trim($(this).text());
          return '<a class="tooltip" href="#">' + term + '<p class="classic"><span>'+term+'</span> '+description+'</p></a>';
        });
      } 
    }
  }); 
});
}
$(document).ready(findTerms);
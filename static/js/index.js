$(document).ready(function() {
  $("input:file").change(function (){
    var filename = $(this).val();
    if (filename.length > 0)
      $(".filename").html(filename);
    else
      $(".filename").html("Browse");
  });
});

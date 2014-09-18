function setSelect(elt, items) {
  $(elt).empty();

  for (var i = 0; i < items.length; i++) {
    $(elt).append('<option>' + items[i] + '</option>');
  }
}

$(document).ready(function() {
  $('select.method').on('change', function() {
    var method = $('select.method').val();
    setSelect('select.type', types[method]);
  });
  setSelect('select.method', methods);
  setSelect('select.type', types[methods[0]]);
  $("input:file").change(function (){
    var filename = $(this).val();
    if (filename.length > 0)
      $(".filename").html(filename);
    else
      $(".filename").html("Browse");
  });
});

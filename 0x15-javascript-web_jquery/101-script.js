$.when($.ready).then(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>NEW ITEM</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list').children('li:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').children('li').remove();
  });
});

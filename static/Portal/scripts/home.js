(function(){

  function add_listing_count(group, count_by_data_attr){
    $(group).each(function(index, element){
      var this_element = $(element),
          listings_count = 0;

      if (count_by_data_attr){
        this_element.find('> ul > li').each(function(index, element){
          listings_count += parseInt($(element).data('listings_count')) || 0;
        });
      } else {
        listings_count = this_element.find('> ul > li').length;  
      }

      if (listings_count > 0){
        this_element.find('> span').append(' <i>('+listings_count+')</i>');
        this_element.data('listings_count', listings_count);
      } else {
        this_element.addClass('unexpandable');
      }
    })
  }

  add_listing_count('ul.parts > li', false);
  add_listing_count('ul.subcategories > li', true);
  add_listing_count('ul.categories > li', true);

  // Expand/collapse on click
  $('li').on('click', function(e){
    if ($(this).hasClass('unexpandable')) return false;

    if (e.target.tagName === 'A') {
      // let anchor tags pass, but no need to bubble up click event
      e.stopPropagation();
    } else {
      $(this).toggleClass('expanded');
      return false;
    }    
  })

}());
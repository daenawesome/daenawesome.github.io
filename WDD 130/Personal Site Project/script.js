$(function () {
    $(".box-hidden").slice(0, 8).show();
    $("loadMore").on('click', function (e){
      e.preventDefault();
      $(".box-hidden:hidden").slice(0,4).sliceDown();
      if ($(".box-hidden:hidden").length == 0) {
          $("#load").fadeOut('slow');
      }
      $('html,body').animate({
        scrollTop: $(this).offset().top
      }, 1500);
      });
    });
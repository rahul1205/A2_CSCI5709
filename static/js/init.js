(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();
 	$('.carousel').carousel();
 	autoplay();
	function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 2000);
}
  }); // end of document ready
})(jQuery); // end of jQuery name space

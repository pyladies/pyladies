$(function() {
	// the element inside of which we want to scroll
        var $elem = $('#content');

        // show the buttons
	$('#nav_up').fadeIn('slow');
	$('#nav_down').fadeIn('slow');  

        // whenever we scroll fade out both buttons
	$(window).bind('scrollstart', function(){
		$('#nav_up,#nav_down').stop().animate({'opacity':'0.2'});
	});
        // ... and whenever we stop scrolling fade in both buttons
	$(window).bind('scrollstop', function(){
		$('#nav_up,#nav_down').stop().animate({'opacity':'1'});
	});

        // clicking the "down" button will make the page scroll to the $elem's height
	$('#nav_down').click(
		function (e) {
			$('html, body').animate({scrollTop: $elem.height()}, 800);
		}
	);
        // clicking the "up" button will make the page scroll to the top of the page
	$('#nav_up').click(
		function (e) {
			$('html, body').animate({scrollTop: '0px'}, 800);
		}
	);
 });
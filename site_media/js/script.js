(function ($) {

	$('header li').hover(
		function () {
			// handler in eventObject - show sub menu
			$('ul', this).slideDown(100);
			console.log($('ul', this));
		}, 
        function () {
			// handler out on eventObject - hide sub menu
			$('ul', this).slideUp(100);
		}
	);

})(jQuery)

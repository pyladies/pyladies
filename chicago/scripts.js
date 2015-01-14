$(document).ready(function() {
	$('a.internal').click(function() {
		event.preventDefault();
		var linkName = this.children[0].className;
		console.log(linkName);

		clickFunction(linkName);
	})

	var clickFunction = function(linkName) {
		var newBlock = "." + linkName + "-block";

			$(newBlock).toggleClass("hidden");
			$(".replace").toggleClass("hidden");
			$(".replace").removeClass("replace")
			$(newBlock).toggleClass("replace");
	}

})
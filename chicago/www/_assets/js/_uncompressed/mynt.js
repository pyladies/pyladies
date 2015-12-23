$(window).load(function () {
    // Preserve vertical rhythm.
    $('.body img').each(function () {
        var
            $this = $(this),
            
            baseline = parseInt($('p').css('line-height'), 10),
            height = $this.outerHeight(true),
            
            remainder = height % baseline;
        
        if (remainder) {
            var
                difference = baseline - remainder,
                margin_top = parseInt($this.css('margin-top'), 10),
                margin_bottom = parseInt($this.css('margin-bottom'), 10);
            
            $this.css('margin-top', margin_top + Math.ceil(difference / 2));
            $this.css('margin-bottom', margin_bottom + Math.floor(difference / 2));
        }
    });
});

$(window).on('load', function () {
    // Preserve vertical rhythm.
    var baseline = 9;
    
    $('.post img, div.code').each(function () {
        var
            $this = $(this),
            $anchor = $this.parent('a'),
            
            margin_top = parseInt($this.css('margin-top'), 10),
            margin_bottom = parseInt($this.css('margin-bottom'), 10),
            
            height = $this.outerHeight(),
            remainder = height % baseline;
        
        if ($anchor.length) {
            margin_bottom += 1;
            
            $anchor.css('border-bottom-width', '0px');
            $this.css('margin-bottom', margin_bottom);
        }
        
        if (remainder) {
            var difference = baseline - remainder;
            
            $this.css('margin-top', margin_top + Math.ceil(difference / 2));
            $this.css('margin-bottom', margin_bottom + Math.floor(difference / 2));
        }
    });
});

(function ($) {
    /**
     * Check a selector exist or not
     */
    $.fn.exists = function () {
        return this.length !== 0;
    };

    /**
     * Close navigation bar when click outside
     */
    $(document).on('click','.navbar-collapse.in',function(e) {
        if( $(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle' ) {
            $(this).collapse('hide');
        };
    });

})(jQuery);

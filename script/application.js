$(document).ready(function(){

    // comprobar si estem dins del puto iframe de la merda de cinfonet
    // i redirigir cap a www.pego.org
    if(!(top === self)){
        top.parent.location.href = 'http://www.pego.org';
    }
    // Cookies policy banner
    var cookiesBanner = $('#cookies-policy');
    var ajupegoCookieName = 'ajupego_cookie_usage_accepted';
    if (docCookies.getItem('ajupego_cookie_usage_accepted') !== null){
        cookiesBanner.addClass('hidden');
    }
    $('#cookies-policy a').click(function (){
        cookiesBanner.addClass('hidden');
        // Do not show cookies banner during one day.
        var tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        docCookies.setItem(ajupegoCookieName, true, tomorrow);
        console.log("cookie set " + docCookies.getItem(ajupegoCookieName));
    });


    $('#menu .menu-section a').each(function(){
        if(this.href == window.location.href){
            $(this).parents('li').addClass('current');
        }
    });

    if ($('.tabs').length > 0) {$('.tabs').tabs();};

    // automatically expand the section menu.toggleClass
    var sectionMatch = /^(http|https):\/\/[\w\.]*(:\d*)*\/([\w-]*)\/*.*$/.exec(window.location.href);
    if(sectionMatch !== null) {
        var section = sectionMatch[3];

        $('#ms_'+section).addClass('expanded');
    }

    $('#menu a.item').click(function (){
        // find the menu to expand.
        var current_menu = $(this).parents('.item-container').find('.menu-section');
        // close all other opened menus.
        $('#menu .menu-section').removeClass('expanded');
        // Open this menu.menu-section
        current_menu.toggleClass('expanded');
        return false;
    });
});
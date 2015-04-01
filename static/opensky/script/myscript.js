$(document).ready(function() {
    $(".fancybox").fancybox({
        afterShow: function() {
            $(".fancybox-title").wrapInner('<div />').show();
            $(".fancybox-wrap").hover(function() {
                $(".fancybox-title").show();
            }, function() {
                $(".fancybox-title").hide();
            });
        },
        helpers : {
            title: {
                type: 'over'
        }
    }});
    $(function () {
        $('#myTab a:first').tab('show');
    });
    //var active = $("li");
    //active.click(function(){
    //    //active.removeClass("active");
    //    $(this).addClass("active");
    //});
});

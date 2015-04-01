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
    $("#myNavbar").find("li").not(".dropdown").children("a").click(function(){
        $(".nav").find("li").removeClass("active");
        $(this).parent().addClass("active");
    });
    var onclick =  $("#myNavbar").find("a").filter(function(){
        return $(this).attr("href") === window.location.pathname;
    })
    onclick.parent().addClass("active");
    onclick.parents(".dropdown").addClass("active");
});

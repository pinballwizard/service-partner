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
        $(this).parents(".dropdown").addClass("active");
    });
    var afterClick =  $("#myNavbar").find("a").filter(function(){
        return $(this).attr("href") == window.location.pathname;
    });
    afterClick.parent().addClass("active");
    afterClick.parents(".dropdown").addClass("active");

//    Google Analitics
    (function(i,s,o,g,r,a,m){
    i['GoogleAnalyticsObject']=r;
    i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();
        a=s.createElement(o),m=s.getElementsByTagName(o)[0];
        a.async=1;
        a.src=g;
        m.parentNode.insertBefore(a,m)
    })
    (window,document,'script','//www.google-analytics.com/analytics.js','ga');
    ga('create', 'UA-61480902-1', 'auto');
    ga('send', 'pageview');

});

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

//    Google maps
    var apiKey = 'AIzaSyDkTrVxNe0ZMrZ0FBNGtO8n0MEyrpB07vI';
//    initialize();
});

function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(-34.397, 150.644),
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
}



//function loadScript() {
//    var script = document.createElement("script");
//    script.type = "text/javascript";
//    script.src = "http://maps.googleapis.com/maps/api/js?key=AIzaSyDkTrVxNe0ZMrZ0FBNGtO8n0MEyrpB07vI&sensor=true";
//    document.body.appendChild(script);
//}

//window.onload = initialize;
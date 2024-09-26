$("h1").after("<h2>Added: </h2>")

$("h3").prepend("Added to the beginning : ");
$("h3").append(" : Added to the end");
$("body").keypress(function(event) {
    var text = $("h2").text();
    $("h2").text(text + event.key);
});

$("h2").on("mouseover", function() {
    $(this).css("color", "red");
});

$("h2").on("mouseleave", function() {
    $(this).css("color", "black");
});

$("button").click(function() {
    $("button").remove();
});

$("#toggle").click(function() {
    $("#toggle>#object").toggle();
});

$("#fadetoggle").click(function() {
    $("#fadetoggle>#object").fadeToggle();
});

$("#slidetoggle").click(function() {
    $("#slidetoggle>#object").slideToggle();
});

$("#animate").click(function() {
    $("#animate>#object").slideUp().slideDown().animate({
        opacity: 0.25,
        height: "toggle"
    }, 5000);
});
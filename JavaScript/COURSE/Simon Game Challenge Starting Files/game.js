var gamePattern = [];
var userClickedPattern = [];

var sequence = [];
var buttonColours = ["red", "blue", "green", "yellow"];

var level = 0;
var currentLevel = 0;

function nextSequence() {
    var randomNumber = Math.floor(Math.random() * 4);
    var randomChosenColour = buttonColours[randomNumber];
    gamePattern.push(randomChosenColour);
    playSound(randomChosenColour);
    animationPress(randomChosenColour);
    level++;
    $("h1").text(`Level ${level}`);
}


function animationPress(color) {
    $(`.btn.${color}`).animate({opacity: 0.2}).delay("fast").animate({opacity: 1}, 100);
}

function playSound(color){
    var sound = new Audio(`sounds/${color}.mp3`);
    sound.play();
}

function checkAnswer(currentLevel) {
    return gamePattern[currentLevel] === userClickedPattern[currentLevel];
}

function clearUser(){
    userClickedPattern = [];
    currentLevel = 0;
}

function startOver() {
    level=0;
    gamePattern = [];
    clearUser();
}

$(".btn").click(function(event) {
    var userChosenColour = event.target.id;
    animationPress(userChosenColour);
    playSound(userChosenColour);
    userClickedPattern.push(userChosenColour);

    if (checkAnswer(currentLevel)){
        currentLevel++;
        if (currentLevel === level) {
            clearUser();
            setTimeout(nextSequence, 1000);
        }
    } else {
        $("body").addClass("game-over");
        setTimeout(()=>{$("body").removeClass("game-over")}, 200);
        $("h1").text("Game Over, Press Any Key to Restart");
        playSound("wrong");
        startOver();
    }
});

$("body").keypress(function() {
        nextSequence();
});

// event listener for mouse click
const bottonsList = document.querySelectorAll("button");
for (var i=0; i<bottonsList.length; i++){
    bottonsList[i].addEventListener("click", function () {
        HighlightKey(this.innerHTML);
        makeSound(this.innerHTML);

    });
}


// event listener for keyboard
document.addEventListener("keydown", function(event){
    HighlightKey(event.key);
    makeSound(event.key);
});


// function to play sound
function makeSound(key){
    
    switch(key){
        case "w":
            var sound = new Audio("sounds/tom-1.mp3");
            break;
        case "a":
            var sound = new Audio("sounds/tom-2.mp3");
            break;
        case "s":
            var sound = new Audio("sounds/tom-3.mp3");
            break;
        case "d":
            var sound = new Audio("sounds/tom-4.mp3");
            break;
        case "j":
            var sound = new Audio("sounds/snare.mp3");
            break;
        case "k":
            var sound = new Audio("sounds/crash.mp3");
            break;
        case "l":
            var sound = new Audio("sounds/kick-bass.mp3");
            break;
        default:
            alert("Error");
            return ;
    }
    sound.play();
}

// function to highlight the key
function HighlightKey(key){
    var activeButton = document.querySelector("."+key);
    activeButton.classList.add("pressed");
    setTimeout(() => {
        activeButton.classList.remove("pressed");
    }, 100);
}
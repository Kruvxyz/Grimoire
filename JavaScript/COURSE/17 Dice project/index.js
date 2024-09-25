

function diceClean(diceEl){
    dotsList = diceEl.querySelectorAll(".dot")
    for (var i = 0; i < dotsList.length; i++){
        dotsList[i].classList.remove("dot_show")
    }
}
function showOne(diceEl){
    diceEl.querySelector(".dot_5").classList.add("dot_show")
}
function showTwo(diceEl){
    diceEl.querySelector(".dot_1").classList.add("dot_show")
    diceEl.querySelector(".dot_9").classList.add("dot_show")
}
function showThree(diceEl){
    diceEl.querySelector(".dot_1").classList.add("dot_show")
    diceEl.querySelector(".dot_5").classList.add("dot_show")
    diceEl.querySelector(".dot_9").classList.add("dot_show")
}
function showFour(diceEl){
    diceEl.querySelector(".dot_1").classList.add("dot_show")
    diceEl.querySelector(".dot_3").classList.add("dot_show")
    diceEl.querySelector(".dot_7").classList.add("dot_show")
    diceEl.querySelector(".dot_9").classList.add("dot_show")
}
function showFive(diceEl){
    diceEl.querySelector(".dot_1").classList.add("dot_show")
    diceEl.querySelector(".dot_3").classList.add("dot_show")
    diceEl.querySelector(".dot_5").classList.add("dot_show")
    diceEl.querySelector(".dot_7").classList.add("dot_show")
    diceEl.querySelector(".dot_9").classList.add("dot_show")
}
function showSix(diceEl){
    diceEl.querySelector(".dot_1").classList.add("dot_show")
    diceEl.querySelector(".dot_3").classList.add("dot_show")
    diceEl.querySelector(".dot_4").classList.add("dot_show")
    diceEl.querySelector(".dot_6").classList.add("dot_show")
    diceEl.querySelector(".dot_7").classList.add("dot_show")
    diceEl.querySelector(".dot_9").classList.add("dot_show")
}

function rollTheDices() {
    var dict1Results = Math.floor(Math.random() * 6);
    var dict2Results = Math.floor(Math.random() * 6);

    const diceOptions = [showOne, showTwo, showThree, showFour, showFive, showSix]

    const dice1 = document.querySelector(".dice_one")
    const dice2 = document.querySelector(".dice_two")
    diceClean(dice1)
    diceClean(dice2)
    diceOptions[dict1Results](dice1)
    diceOptions[dict2Results](dice2)
    
}
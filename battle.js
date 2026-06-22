console.log("Battle JS Connected!");

let battleStarted = false;
let playerPower = 0;

function openWeapons() {


document.getElementById("weaponPanel").style.display = "block";


}

function closeWeapons() {


document.getElementById("weaponPanel").style.display = "none";


}

function playAnimation(form) {


closeWeapons();

battleStarted = false;

playerPower = 0;

window.currentForm = form;

document.getElementById(
    "tapBattle"
).style.display = "block";


}

function startParticleStorm(){


let area =
    document.getElementById("battleAnimation");

area.innerHTML = "";

area.style.display = "block";

let storm = setInterval(function(){

    let p =
        document.createElement("div");

    p.className =
        "particle player-particle";

    p.style.setProperty(
        "--curve",
        (Math.random()*300 - 150) + "px"
    );

    p.style.animation =
        "flyRight 1.2s linear forwards";

    area.appendChild(p);

    let a =
        document.createElement("div");

    a.className =
        "particle ai-particle";

    a.style.setProperty(
        "--curve",
        (Math.random()*300 - 150) + "px"
    );

    a.style.animation =
        "flyLeft 1.2s linear forwards";

    area.appendChild(a);

    setTimeout(function(){

        p.remove();
        a.remove();

    },1200);

},40);

let powerStorm = setInterval(function(){

    for(let i = 0; i < playerPower/5; i++){

        let p =
            document.createElement("div");

        p.className =
            "particle player-particle";

        p.style.setProperty(
            "--curve",
            (Math.random()*300 - 150) + "px"
        );

        p.style.animation =
            "flyRight .5s linear forwards";

        area.appendChild(p);

        setTimeout(function(){

            p.remove();

        },500);

    }

},100);

setTimeout(function(){

    clearInterval(storm);

    clearInterval(powerStorm);

    let splash =
        document.createElement("div");

    splash.className =
        "energy-splash";

    area.appendChild(splash);

    document.getElementById(
        "tapBattle"
    ).style.display = "none";

    setTimeout(function(){

        window.location =
            window.currentForm.action;

    },1000);

},5000);


}

document.addEventListener(
"DOMContentLoaded",
function(){


let btn =
    document.getElementById("tapBtn");

if(btn){

    btn.onclick = function(){

        if(!battleStarted){

            battleStarted = true;

            startParticleStorm();

        }

        playerPower += 5;

        document.getElementById(
            "powerText"
        ).innerHTML =
        "REACTOR POWER : " +
        playerPower;

    };

}


});

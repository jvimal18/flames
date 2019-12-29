const result = document.getElementById("result")
const submit = document.getElementById("submit")
document.getElementById("body").style.height = window.innerHeight + "px"
document.getElementById("body").style.width = window.innerWidth + "px"

window.addEventListener("resize", function () {
    document.getElementById("body").style.height = window.innerHeight + "px"
    document.getElementById("body").style.width = window.innerWidth + "px"
    console.log("triggered resize")
})

submit.addEventListener("click", function () {
    const male = document.getElementById("male").value
    const female = document.getElementById("female").value
    if (!male) { alert("Please enter your name ") }
    else if (!female) { alert("Please enter your name ") }
    else {
        execute(male, female)
    }
})

function execute(male, female) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            result.innerHTML = "<h1>" + this.responseText + "</h1>";
        }
    };
    xhttp.open("GET", "/flames?male="+male+"&female="+female, true);
    xhttp.send();
}


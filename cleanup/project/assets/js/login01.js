// Select elements
const popuplog = document.getElementById("login");
const popupblurlog = document.getElementById("loginnowblur");


// Open first popup
function openpoplogin() {


    // add classes
    popuplog.classList.add("conformloginopen-popup");
    popupblurlog.classList.add("containerblurloginopen-popup");

}


// Switch to calculation popup
function popcals() {


    // Close first popup
    popuplog.classList.remove("conformloginopen-popup");
    popupblurlog.classList.remove("containerblurloginopen-popup");


}


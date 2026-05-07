// Select elements
const popup = document.getElementById("booknow");
const popupblur = document.getElementById("booknowblur");


// Open first popup
function openpopbook() {


    // add classes
    popup.classList.add("conformbookopen-popup");
    popupblur.classList.add("containerbluropen-popup");

}


// Switch to calculation popup
function popcals() {


    // Close first popup
    popup.classList.remove("conformbookopen-popup");
    popupblur.classList.remove("containerbluropen-popup");


}



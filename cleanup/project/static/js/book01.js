// Select elements
const popup = document.getElementById("booknow");
const popupblur = document.getElementById("booknowblur");
const popupcal = document.getElementById("concalculation");


// Open first popup
function openpopbook() {
    popup.classList.add("conformbookopen-popup");
    popupblur.classList.add("containerbluropen-popup");
}


// Switch to calculation popup
function popcals() {
    popupcal.classList.add("concalculationopen-popup");

    // Close first popup
    //popup.classList.remove("conformbookopen-popup");
    //popupblur.classList.remove("containerbluropen-popup");
}

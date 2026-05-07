let opup = document.getElementById("alertpopup");

function openpop() {
    // Show the popup
    opup.classList.add("alertopen-popup");

    // Hide it automatically after 3 seconds
    setTimeout(() => {
        opup.classList.remove("alertopen-popup");
    }, 1000);
}

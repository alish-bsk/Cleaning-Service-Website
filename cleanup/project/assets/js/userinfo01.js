
const names = ["Lisa Anderson","Riyan Tarhan","John Carter","James Christ"];
const year = ["4 years ago","5 years ago","2 years ago","6 years ago"];
const descr = ["Excellent service! The work was completed 100%, quickly and efficiently.Thank you for the professional approach.","Outstanding service! The job was completed perfectly, with speed and efficiency.Thank you for your professional approach","Truly excellent work — everything was finished 100% on time, quickly and with great care.  I appreciate the professionalism!","Fantastic experience! The team delivered flawless results, fast and efficiently.Thank you for handling everything so professionally."];

let index = 4;

document.getElementById("next").addEventListener("click", () => {
  rotate(1);
});
document.getElementById("prev").addEventListener("click", () => {
  rotate(-1);
});

function rotate(direction) {
  const cards = document.querySelectorAll(".cards-wrapper .card");
console.log(cards);

  index = (index + direction + 4) % 4;
  

  const classes = ["far-left","left","center","right"];
    cards.forEach((c, i) => {
        c.className = "card " + classes[(i - index + 4) % 4];

    });
  document.getElementById("name").textContent = names[index];
  document.getElementById("year").textContent = year[index];
  document.getElementById("description").textContent = descr[index];

}

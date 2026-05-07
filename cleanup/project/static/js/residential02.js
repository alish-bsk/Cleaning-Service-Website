/// for scale animation img-choose

window.addEventListener('scroll', function () {
    const itemhand = document.getElementById("hand-imge");
    const itemgirl = document.getElementById("girl-imge");

    const scrollY = window.scrollY;

if (window.scrollY >100) {      
    itemhand.classList.add('visible');
    itemgirl.classList.add('visible');

    } 
    else {
      itemhand.classList.remove('visible');
      itemgirl.classList.remove('visible');

    }
    });



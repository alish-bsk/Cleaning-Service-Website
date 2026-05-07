  // for top background///
  window.addEventListener('scroll', function () {
    const item = document.getElementById('topscrollItem');
    const scrollY = window.scrollY;

    if (scrollY > 100) { // Adjust this value as needed
      item.classList.add('visible');
    } else {
      item.classList.remove('visible');
    }
    
  });


  /// for card service////


  //for X direction animation
  window.addEventListener('scroll', function () {
    const item = document.getElementById('services-cardonex');
    const itemtw = document.getElementById('services-cardtwx');
    const itemthre = document.getElementById('services-cardthrex');
    const itemfur = document.getElementById('services-cardfurx');


    const scrollY = window.scrollY;

    if (scrollY > 100) { // Adjust this value as needed
      item.classList.add('visible');
      itemtw.classList.add('visible');
      itemthre.classList.add('visible');
      itemfur.classList.add('visible');


    } else {
      item.classList.remove('visible');
      itemtw.classList.remove('visible');
      itemthre.classList.add('visible');
      itemfur.classList.add('visible');

    }
    
  });

  //for y direction animation
  window.addEventListener('scroll', function () {
    const item = document.getElementById('services-cardonexpos');
    const itemtw = document.getElementById('services-cardtwxpos');
    const itemthre = document.getElementById('services-cardthrexpos');


    const scrollY = window.scrollY;

    if (scrollY > 100) { // Adjust this value as needed
      item.classList.add('visible');
      itemtw.classList.add('visible');
      itemthre.classList.add('visible');


    } else {
      item.classList.remove('visible');
      itemtw.classList.remove('visible');
      itemthre.classList.add('visible');

    }
    
  });


    //for center direction animation
  window.addEventListener('scroll', function () {
    const item = document.getElementById('services-cardonecen');
    const itemtw = document.getElementById('services-cardtwcen');
    const itemthre = document.getElementById('services-cardthrecen');


    const scrollY = window.scrollY;

    if (scrollY > 100) { // Adjust this value as needed
      item.classList.add('visible');
      itemtw.classList.add('visible');
      itemthre.classList.add('visible');


    } else {
      item.classList.remove('visible');
      itemtw.classList.remove('visible');
      itemthre.classList.add('visible');

    }
    
  });

  //for choose us animation

  /// for choose us visible
    window.addEventListener('scroll', function () {
    const item = document.getElementById('choosescrollitem');
    const sectionTop = document.querySelector("#choose-us").offsetTop;
    const scrollY = window.scrollY;

if (window.scrollY >sectionTop-200) {      
    item.classList.add('visible');
    } else {
      item.classList.remove('visible');
    }
    
  });
    /// for translate x animation img-first

window.addEventListener('scroll', function () {
    const item = document.getElementById('img-first');
    const sectionTop = document.querySelector("#choose-us").offsetTop;
    const scrollY = window.scrollY;

if (window.scrollY >sectionTop-200) {      
    item.classList.add('visible');
    } 
    else {
      item.classList.remove('visible');
    }
    });


    /// for translate x animation img-scd

    window.addEventListener('scroll', function () {
    const item = document.getElementById('img-scd');
    const sectionTop = document.querySelector("#choose-us").offsetTop;
    const scrollY = window.scrollY;

if (window.scrollY >sectionTop-200) {      
    item.classList.add('visible');
    } 
    else {
      item.classList.remove('visible');
    }
    });


/// for translate x animation choose-us


window.addEventListener('scroll', function () {
    const item = document.getElementById('choose-us');
    const sectionTop = document.querySelector("#choose-us").offsetTop;
    const scrollY = window.scrollY;

if (window.scrollY >sectionTop-200) {      
    item.classList.add('visible');
    } 
    else {
      item.classList.remove('visible');
    }
    });


    /// for translate x animation img-choose

    window.addEventListener('scroll', function () {
    const item = document.getElementById('img-choose');
    const sectionTop = document.querySelector("#choose-us").offsetTop;
    const scrollY = window.scrollY;

if (window.scrollY >sectionTop-200) {      
    item.classList.add('visible');
    } 
    else {
      item.classList.remove('visible');
    }
    });


//    /// for scroll  about us animation 
    window.addEventListener('scroll', function () {
    const itemabut = document.getElementById('aboutuscont');
    const sectionTop = document.querySelector("#aboutuscont").offsetTop;
    const scrollY = window.scrollY;
    console.log(scrollY);
    

if (scrollY >sectionTop-100) {      
    itemabut.classList.add('visible');
    } 
    else {
      itemabut.classList.remove('visible');
    }
    
    });



    //    /// for guarantee text  about us animation 

    window.addEventListener('scroll', function () {
    const itemgu = document.getElementById('text-guarantee');
    const sectionTop = document.querySelector("#text-guarantee").offsetTop;
    const scrollY = window.scrollY;
    console.log(scrollY);
    

if (scrollY >sectionTop-200) {      
    itemgu.classList.add('visible');
    } 
    else {
      itemgu.classList.remove('visible');
    }
    
    });

    //    /// for guarantee bond text  about us animation 
    window.addEventListener('scroll', function () {
    const itemgu = document.getElementById('text-sectlab');
    const sectionTop = document.querySelector("#text-sectlab").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemgu.classList.add('visible');
    } 
    else {
      itemgu.classList.remove('visible');
    }
    
    });


        //    /// for guarantee term conditon text  about us animation 
    window.addEventListener('scroll', function () {
    const itemgu = document.getElementById('text-content');
    const sectionTop = document.querySelector("#text-content").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemgu.classList.add('visible');
    } 
    else {
      itemgu.classList.remove('visible');
    }
    
    });

        //    /// for guarantee term conditon text  about us animation 

    window.addEventListener('scroll', function () {
    const itemgu = document.getElementById('sidebar-one');
    const sectionTop = document.querySelector("#sidebar-one").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemgu.classList.add('visible');
    } 
    else {
      itemgu.classList.remove('visible');
    }
    
    });

        window.addEventListener('scroll', function () {
    const itemgutw = document.getElementById('sidebar-tw');
    const sectionTop = document.querySelector("#sidebar-tw").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-300) {      
    itemgutw.classList.add('visible');
    } 
    else {
      itemgutw.classList.remove('visible');
    }
    
    });

//    /// for guarantee  text-commitment text  about us animation 

window.addEventListener('scroll', function () {
    const itemgu = document.getElementById('text-commitment');
    const itemgutw = document.getElementById('text-commitmenttw');

    const sectionTop = document.querySelector("#text-commitment").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemgu.classList.add('visible');
    itemgutw.classList.add('visible');

    } 
    
else {
      itemgu.classList.remove('visible');
      itemgutw.classList.remove('visible');

    }
    
    });

// for reasoncard


window.addEventListener('scroll', function () {
    const itemcdone = document.getElementById('commitment-cardone');
    const itemcdtw = document.getElementById('commitment-cardtw');
    const itemcdthr = document.getElementById('commitment-cardthr');
    const itemcdfur = document.getElementById('commitment-cardfur');


    const sectionTop = document.querySelector("#commitment-cardone").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemcdone.classList.add('visible');
    itemcdtw.classList.add('visible');
    itemcdthr.classList.add('visible');
    itemcdfur.classList.add('visible');


    } 
    
else {
      itemcdone.classList.remove('visible');
      itemcdtw.classList.remove('visible');
      itemcdthr.classList.remove('visible');
      itemcdfur.classList.remove('visible');

    }
    
    });


    //    /// for book now  text-book text  about us animation 
window.addEventListener('scroll', function () {
    const itembkone = document.getElementById('text-bookone');
    const itembktw = document.getElementById('text-booktw');
    const itembtnone = document.getElementById('btn-bookone');


    const sectionTop = document.querySelector("#text-bookone").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itembkone.classList.add('visible');
    itembktw.classList.add('visible');
    itembtnone.classList.add('visible');


    } 
    
else {
      itembkone.classList.remove('visible');
      itembktw.classList.remove('visible');
      itembtnone.classList.remove('visible');

    }
    
    });


    //    /// for book now  text-address text  about us animation 


window.addEventListener('scroll', function () {
    const itemadct = document.getElementById('card-contact');
    const itemadma = document.getElementById('card-email');
    const itemadqt= document.getElementById('card-quote');


    const sectionTop = document.querySelector("#card-contact").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemadct.classList.add('visible');
    itemadma.classList.add('visible');
    itemadqt.classList.add('visible');


    } 
    
else {
      itemadct.classList.remove('visible');
      itemadma.classList.remove('visible');
      itemadqt.classList.remove('visible');

    }
    
    });



//    /// for book now  send us message text  about us animation 
window.addEventListener('scroll', function () {
    const itemadmsg = document.getElementById('card-msg');


    const sectionTop = document.querySelector("#card-msg").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemadmsg.classList.add('visible');


    } 
    
else {
      itemadmsg.classList.remove('visible');

    }
    
    });

//    /// for book now  question text  about us animation 


window.addEventListener('scroll', function () {
    const itemqusone = document.getElementById('text-quick');
    const itemqustw = document.getElementById('text-quicktw');

    const itemqusrlone = document.getElementById('card-quesone');
    const itemqusrltw = document.getElementById('card-questw');
    const itemqusrlthr = document.getElementById('card-questhr');
    const itemqusrlfur = document.getElementById('card-quesfur');



    const sectionTop = document.querySelector("#text-quick").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemqusone.classList.add('visible');
    itemqustw.classList.add('visible');

    itemqusrlone.classList.add('visible');
    itemqusrltw.classList.add('visible');
    itemqusrlthr.classList.add('visible');
    itemqusrlfur.classList.add('visible');



    } 
    
else {
      itemqusone.classList.remove('visible');
      itemqustw.classList.remove('visible');


      itemqusrlone.classList.remove('visible');
      itemqusrltw.classList.remove('visible');
      itemqusrlthr.classList.remove('visible');
      itemqusrlfur.classList.remove('visible');

    }
    
    });

//    /// for book now  footer text  about us animation 

window.addEventListener('scroll', function () {
    const itemft = document.getElementById('footer-clean');

    const sectionTop = document.querySelector("#footer-clean").offsetTop;
    const scrollY = window.scrollY;
    

if (scrollY >sectionTop-200) {      
    itemft.classList.add('visible');


    } 
    
else {
      itemft.classList.remove('visible');



    }
    
    });

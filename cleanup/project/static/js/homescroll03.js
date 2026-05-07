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
  window.addEventListener('scroll', function () {
    const item = document.getElementById('choosescrollitem');


    const scrollY = window.scrollY;

    if (scrollY > 100) { // Adjust this value as needed
      item.classList.add('visible');


    } else {
      item.classList.remove('visible');

    }
    
  });
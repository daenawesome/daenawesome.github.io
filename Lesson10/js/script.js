
function showForecast() {
    const forecast = document.querySelector('.forecast');
    const forecastHeader = document.querySelector('#forecast-header');
    const arrow = document.querySelector('#forecast-header p');

    forecastHeader.addEventListener('click', () => {
        // Only toggle the class if we are on the small view size
        if (window.matchMedia("(min-width: 768px)").matches || window.matchMedia("(min-width: 1024px)").matches)
            return;
        forecast.classList.toggle('show');
        // Flip the arrow around
        if (forecast.classList.contains('show'))
            arrow.innerHTML = "&#9651;";
        else
            arrow.innerHTML = "&#9661;";
    });
}

function showPancakes(day) {
    // Only show the pancake message if it is Friday
    if (day == "Friday") {
        const pancakes = document.querySelector('.pancakes');
        pancakes.style.display = "grid";
    }
    return;
}

window.addEventListener('load', () => {
    // Create responsive nav
    const hambutton = document.querySelector('.ham');
    const mainnav = document.querySelector('#navigation');

    hambutton.addEventListener('click', () => {
        mainnav.classList.toggle('responsive')
    }, false);

    // To resolve the mid resizing issue with class on
    window.onresize = () => {
        if (window.innerWidth > 768) mainnav.classList.remove('responsive')
    };

    // Set the date on the footer
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const date = new Date();
    const day = days[date.getDay()];
    const month = months[date.getMonth()];
    document.querySelector('.footer-bottom').innerHTML = day + ", " + date.getDate() + " " + month + " " + date.getFullYear();
    
    showPancakes(day);
    showForecast();
});


// Image load on scroll
let imagesToLoad = document.querySelectorAll('img[data-src]');
const loadImages = (image) => {
  image.setAttribute('src', image.getAttribute('data-src'));
  image.onload = () => {
    image.removeAttribute('data-src');
  };
};

const imgOptions = {
  threshold: 0.5,
  rootMargin: "0px 0px -100px 0px"
};

if('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((items, observer) => {
    items.forEach((item) => {
      if(item.isIntersecting) {
        loadImages(item.target);
        observer.unobserve(item.target);
      }
    });
  }, imgOptions);


  imagesToLoad.forEach((img) => {
    observer.observe(img);
  });
} else {
  imagesToLoad.forEach((img) => {
    loadImages(img);
  });
}

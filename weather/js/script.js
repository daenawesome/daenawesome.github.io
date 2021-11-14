function showForecast() {
    const forecast = document.querySelector('.forecast');
    const forecastHeader = document.querySelector('#forecast-header');
    const arrow = document.querySelector('#forecast-header p');

    forecastHeader.addEventListener('click', () => {
        // Only toggle the class if we are on the small view size
        if (window.matchMedia("(min-width: 768px)").matches || window.matchMedia("(min-width: 1024px)").matches)
            return;
        forecast.classList.toggle('show');
        if (forecast.classList.contains('show'))
            arrow.innerHTML = "&#9651;";
        else
            arrow.innerHTML = "&#9661;";
    });
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
        if (window.innerWidth > 760) mainnav.classList.remove('responsive')
    };

    // Set the date on the footer
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const date = new Date();
    const day = days[date.getDay()];
    const month = months[date.getMonth()];
    document.querySelector('.footer-bottom').innerHTML = day + ", " + date.getDate() + " " + month + " " + date.getFullYear();

    showForecast();
});
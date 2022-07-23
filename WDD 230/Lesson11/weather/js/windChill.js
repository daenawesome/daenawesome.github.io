window.addEventListener('load', () => {
    let element = document.querySelector('#wind-chill');
    let tempature = document.querySelector('#tempature').innerHTML;
    let windSpeed = document.querySelector('#wind-speed').innerHTML;
    let windChill = 0;

    if (tempature <= 45 && windSpeed > 3) {
        windChill = Math.round(35.74 + 0.6215 * tempature - 35.75 * Math.pow(windSpeed, 0.16) + 0.4275 * tempature * Math.pow(windSpeed, 0.16));
        element.innerHTML = windChill;
    } else {
        element.innerHTML = tempature;
    }
})
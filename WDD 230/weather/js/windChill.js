window.addEventListener('load', () => {
    let element = document.querySelector('#wind-chill');
    let temperature = document.querySelector('#temperature').innerHTML;
    let windSpeed = document.querySelector('#wind-speed').innerHTML;
    let windChill = 0;

    if (temperature <= 45 && windSpeed > 3) {
        windChill = Math.round(35.74 + 0.6215 * temperature - 35.75 * Math.pow(windSpeed, 0.16) + 0.4275 * temperature * Math.pow(windSpeed, 0.16));
        element.innerHTML = windChill + "°F";
    } else {
        element.innerHTML = "N/A";
    }
})

async function getFiveDay() {
    const url = "https://api.openweathermap.org/data/2.5/forecast?id=5604473&units=imperial&appid=d74b44aa3356c559c263a8574eb61950";

    const response = await fetch(url);
    if (response.status == 200) {
        return response.json();
    } else {
        throw new Error("No weather found: " + response.status);
    }
}

async function getCurrWeather() {
    const url = "https://api.openweathermap.org/data/2.5/weather?id=5604473&units=imperial&appid=d74b44aa3356c559c263a8574eb61950";

    const response = await fetch(url);
    if (response.status == 200) {
        return response.json();
    } else {
        throw new Error("No weather found: " + response.status);
    }
}

function weather() {
    getCurrWeather()
    .then((w) => {
        console.log(w);

        let currHigh = document.querySelector('#tempature');
        let humidity = document.querySelector('#humidity');
        let windSpeed = document.querySelector('#wind-speed');
        let weatherDesc = document.querySelector('#weather-desc'); 

        weatherDesc.textContent = w.weather[0].main;
        currHigh.textContent = Math.floor(w.main.temp);
        humidity.textContent = w.main.humidity;
        windSpeed.textContent = w.wind.speed;
    });

    getFiveDay()
    .then((w) => {
        console.log(w);

        let dayNum = 1;
        for (item of w.list) {
            if (item.dt_txt.includes("18:00:00")) {
                let day = document.querySelector('#day' + dayNum + " .temp");
                let dayDesc = document.querySelector('#day' + dayNum + " .day-desc");
                let dayImg = document.querySelector('#day' + dayNum + " img");

                day.textContent = Math.floor(item.main.temp);
                dayDesc.textContent = item.weather[0].main;
                dayImg.setAttribute('src', "http://openweathermap.org/img/wn/" + item.weather[0].icon + "@2x.png")

                dayNum++;
            }
        }
    });
}

window.addEventListener('load', weather());
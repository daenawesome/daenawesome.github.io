async function getTownData() {
    const url = "https://byui-cit230.github.io/weather/data/towndata.json";

    const response = await fetch(url);
    if (response.status == 200) {
        return response.json()
    } else {
        throw new Error("No town data found " + response.status)
    }
}

function townData() {
    const data = getTownData()
        .then(function(town) {
            console.log(town);

            // Find the index for the towns
            for (item in town["towns"]) {
                if (town["towns"][item].name == "Preston")
                    var prs = item;
                else if (town["towns"][item].name == "Fish Haven")
                    var fh = item;
                else if (town["towns"][item].name == "Soda Springs")
                    var sd = item;
            }

            // Select the places we want to add info
            const prestonImgBox = document.querySelector('#preston');
            const fishHavenImgBox = document.querySelector('#fish-haven');
            const sodaSpringsImgBox = document.querySelector('#soda-springs');
            const preston = document.querySelector('#preston .town-info');
            const fishHaven = document.querySelector('#fish-haven .town-info');
            const sodaSprings = document.querySelector('#soda-springs .town-info');

            // Create the elements
            let prestonMotto = document.createElement('h3');
            let fishHavenMotto = document.createElement('h3');
            let sodaSpringsMotto = document.createElement('h3');

            let prestonYearFounded = document.createElement('p');
            let fishHavenYearFounded = document.createElement('p');
            let sodaSpringsYearFounded = document.createElement('p');

            let prestonPopulation = document.createElement('p');
            let fishHavenPopulation = document.createElement('p');
            let sodaSpringsPopulation = document.createElement('p');

            let prestonRain = document.createElement('p');
            let fishHavenRain = document.createElement('p');
            let sodaSpringsRain = document.createElement('p');

            let prestonImg = document.createElement('img');
            let fishHavenImg = document.createElement('img');
            let sodaSpringsImg = document.createElement('img');

            // Set the elements content
            prestonMotto.textContent = town["towns"][prs].motto;
            fishHavenMotto.textContent = town["towns"][fh].motto;
            sodaSpringsMotto.textContent = town["towns"][sd].motto;
            prestonMotto.classList.add('motto');
            fishHavenMotto.classList.add('motto');
            sodaSpringsMotto.classList.add('motto');

            prestonYearFounded.textContent = "Year Founded: " + town["towns"][prs].yearFounded;
            fishHavenYearFounded.textContent = "Year Founded: " + town["towns"][fh].yearFounded;
            sodaSpringsYearFounded.textContent = "Year Founded: " + town["towns"][sd].yearFounded;

            prestonPopulation.textContent = "Population: " + town["towns"][prs].currentPopulation;
            fishHavenPopulation.textContent = "Population: " + town["towns"][fh].currentPopulation;
            sodaSpringsPopulation.textContent = "Population: " + town["towns"][sd].currentPopulation;

            prestonRain.textContent = "Annual Rain Fall: " + town["towns"][prs].averageRainfall;
            fishHavenRain.textContent = "Annual Rain Fall: " + town["towns"][fh].averageRainfall;
            sodaSpringsRain.textContent = "Annual Rain Fall: " + town["towns"][sd].averageRainfall;

            prestonImg.setAttribute('src', "images/home/" + town["towns"][prs].photo);
            fishHavenImg.setAttribute('src', "images/home/" + town["towns"][fh].photo);
            sodaSpringsImg.setAttribute('src', "images/home/" + town["towns"][sd].photo);

            prestonImg.setAttribute('alt', "preston-img");
            fishHavenImg.setAttribute('alt', "fishHaven-img");
            sodaSpringsImg.setAttribute('alt', "sodaSprings-img");

            // Append the elements
            preston.appendChild(prestonMotto);
            fishHaven.appendChild(fishHavenMotto);
            sodaSprings.appendChild(sodaSpringsMotto);

            preston.appendChild(prestonYearFounded);
            fishHaven.appendChild(fishHavenYearFounded);
            sodaSprings.appendChild(sodaSpringsYearFounded);

            preston.appendChild(prestonPopulation);
            fishHaven.appendChild(fishHavenPopulation);
            sodaSprings.appendChild(sodaSpringsPopulation);

            preston.appendChild(prestonRain);
            fishHaven.appendChild(fishHavenRain);
            sodaSprings.appendChild(sodaSpringsRain);

            prestonImgBox.appendChild(prestonImg);
            fishHavenImgBox.appendChild(fishHavenImg);
            sodaSpringsImgBox.appendChild(sodaSpringsImg);
        }
        );
}

townData();
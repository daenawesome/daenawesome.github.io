// Attach event listener to the search form submit event
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get user input from the search input field
    const userInput = document.getElementById('searchInput').value;
  
    // Encode the user input to be used in the URL
    const title = encodeURIComponent(userInput);
  
    // Set the default page number
    const page = '1';
  
    // Create the URL for the API request
    const url = `https://ott-details.p.rapidapi.com/search?title=${title}&page=${page}`;
  
    // Set the options for the fetch request
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '4955cfa1e9msh3b2611741f0de71p13af46jsn59bec143a4f3',
            'X-RapidAPI-Host': 'ott-details.p.rapidapi.com'
        }
    };
  
    // Fetch data from the API
    fetch(url, options)
        .then(response => response.json()) // Parse response as JSON
        .then(data => {
            console.log(data); // Log the data to the console
  
            // Clear the movies container to remove previous search results
            const moviesContainer = document.querySelector('.movies');
            moviesContainer.innerHTML = '';
  
            // Get the filterReleased element and its selected value
            const filterReleased = document.getElementById('filterReleased');
            const selectedValue = filterReleased.value;
  
            // Filter the movies based on the selected release year range
            const filteredMovies = selectedValue ? data.results.filter(movie => {
              const releasedYear = new Date(movie.released).getFullYear();
              if (selectedValue === '2019-2000') {
                  return releasedYear >= 2000 && releasedYear <= 2019;
              } else {
                  const [startYear, endYear] = selectedValue.split('-');
                  return releasedYear >= parseInt(endYear) && releasedYear <= parseInt(startYear);
              }
            }) : data.results;
  
            // Check if there are filtered movies
            if (filteredMovies.length > 0) {
                // Display the filter container
                const filterContainer = document.getElementById('filterContainer');
                filterContainer.style.display = 'block';
            } else {
                // Display "No Results" message
                moviesContainer.innerHTML = '<h2>No Results</h2>';
                // Hide the filter container
                const filterContainer = document.getElementById('filterContainer');
                filterContainer.style.display = 'none';
            }
  
            // Iterate over each filtered movie and create HTML elements for display
            filteredMovies.forEach(movie => {
                const { title, genre, released, type, synopsis, imageurl, imdbid } = movie;
  
                // Filter out movies with no image or synopsis
                if (!imageurl || imageurl.length === 0 || !synopsis || synopsis.length === 0) {
                    return;
                }
  
                // Create a movie element and set its class
                const movieElement = document.createElement('div');
                movieElement.classList.add('movie');
  
                // Set the inner HTML of the movie element
                movieElement.innerHTML = `
                <img class="backdrop1" src="${imageurl}">
                <img class="backdrop2" src="${imageurl}">    
                <img class="backdrop3" src="${imageurl}">    
                <img class="backdrop4" src="${imageurl}">
                <img class="backdrop5" src="${imageurl}">     
  
                <div class="card">
                    <div class="image"><img src="${imageurl}"></div>
                    <div class="detail">
                        <h2>${title}</h2>
                        <p>${genre.join(', ')}</p>
                        <p data-info="released">${released}</p>
                        <p data-info="type">${type}</p>
                        <p>${synopsis}</p>
                        <a href="#" class="streaming-link" data-imdbid="${imdbid}">Streaming Availability</a><br>
                        <div class="platforms-container"></div>
                    </div>
                </div>
                `;
  
                // Attach event listener to the streaming link
                movieElement.querySelector('.streaming-link').addEventListener('click', function(event) {
                    event.preventDefault();
                    const imdbid = this.getAttribute('data-imdbid');
                    fetchStreamingAvailability(imdbid, movieElement);
                });
  
                // Append the movie element to the movies container
                moviesContainer.appendChild(movieElement);
            });
        })
        .catch(error => {
            console.error(error); // Log any errors to the console
        });
  });
  
  // Function to fetch streaming availability for a movie
  function fetchStreamingAvailability(imdbid, container) {
    // Create the URL for the API request
    const url = `https://ott-details.p.rapidapi.com/gettitleDetails?imdbid=${encodeURIComponent(imdbid)}`;
  
    // Set the options for the fetch request
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '4955cfa1e9msh3b2611741f0de71p13af46jsn59bec143a4f3',
            'X-RapidAPI-Host': 'ott-details.p.rapidapi.com'
        }
    };
  
    // Fetch data from the API
    fetch(url, options)
        .then(response => response.json()) // Parse response as JSON
        .then(data => {
            const streamingAvailability = data.streamingAvailability;
            const countryData = streamingAvailability.country;
            const usData = countryData.US;
  
            // Extract platforms and their URLs from the response data
            const platforms = usData.map(platform => ({
                platform: platform.platform,
                url: platform.url
            }));
  
            // Get the container element for the platforms
            const containerElement = container.querySelector('.platforms-container');
  
            // Check if there are available platforms
            if (platforms.length === 0) {
                containerElement.textContent = 'N/A';
            } else {
                // Create HTML links for each platform
                const links = platforms.map(platform => {
                    const capitalizedPlatform = platform.platform.toUpperCase();
                    const link = document.createElement('a');
                    link.href = platform.url;
                    link.textContent = capitalizedPlatform;
                    return link.outerHTML;
                });
  
                // Set the inner HTML of the container with the platform links
                containerElement.innerHTML = links.join(', ');
            }
        })
        .catch(error => {
            console.error(error); // Log any errors to the console
            const containerElement = container.querySelector('.platforms-container');
            containerElement.textContent = 'N/A';
        });
  }
  
  // Attach event listener to the clear button click event
  document.getElementById('clearButton').addEventListener('click', function() {
      const moviesContainer = document.querySelector('.movies');
      moviesContainer.innerHTML = ''; // Clear the movies container
      document.getElementById('filterReleased').selectedIndex = 0; // Reset the release year filter
      document.getElementById('filterType').selectedIndex = 0; // Reset the type filter
      document.getElementById('searchInput').value = ''; // Clear the search input field
  });
  
  // Attach event listener to the release year filter change event
  document.getElementById('filterReleased').addEventListener('change', function() {
      const moviesContainer = document.querySelector('.movies');
      const filterReleased = document.getElementById('filterReleased');
      const selectedValue = filterReleased.value;
  
      const movieElements = moviesContainer.querySelectorAll('.movie');
      movieElements.forEach(movieElement => {
          const releaseYear = new Date(movieElement.querySelector('p[data-info="released"]').textContent.trim()).getFullYear();
          if (selectedValue === '' || selectedValue === '2019-2000' && releaseYear >= 2000 && releaseYear <= 2019 || selectedValue !== '2019-2000' && releaseYear >= parseInt(selectedValue.split('-')[1]) && releaseYear <= parseInt(selectedValue.split('-')[0])) {
              movieElement.style.display = 'block'; // Show the movie element
          } else {
            movieElement.style.display = 'none'; // Hide the movie element
            // moviesContainer.innerHTML = '<h2>No Results</h2>';
          }
      });
  });
  
  // Attach event listener to the type filter change event
  document.getElementById('filterType').addEventListener('change', function() {
      const moviesContainer = document.querySelector('.movies');
      const filterReleased = document.getElementById('filterReleased');
      const filterType = document.getElementById('filterType');
      const selectedReleased = filterReleased.value;
      const selectedType = filterType.value;
  
      const movieElements = moviesContainer.querySelectorAll('.movie');
      movieElements.forEach(movieElement => {
          const releaseYear = movieElement.querySelector('p[data-info="released"]').textContent.trim();
          const type = movieElement.querySelector('p[data-info="type"]').textContent.trim();
          const matchesReleased = selectedReleased === '' || selectedReleased === releaseYear || (selectedReleased === '2019-2000' && releaseYear >= '2000' && releaseYear <= '2019');
          const matchesType = selectedType === '' || selectedType === type;
          if (matchesReleased && matchesType) {
              movieElement.style.display = 'block'; // Show the movie element
          } else {
              movieElement.style.display = 'none'; // Hide the movie element
          }
      });
  });
  
  // Attach event listener to the sort order change event
  document.getElementById('sortOrder').addEventListener('change', function() {
      const moviesContainer = document.querySelector('.movies');
      const sortOrder = document.getElementById('sortOrder').value;
      const movieElements = Array.from(moviesContainer.querySelectorAll('.movie'));
  
      // Sort the movie elements based on the title
      movieElements.sort((a, b) => {
          const titleA = a.querySelector('h2').textContent.trim();
          const titleB = b.querySelector('h2').textContent.trim();
  
          if (sortOrder === 'asc') {
              return titleA.localeCompare(titleB, 'en', { numeric: true }); // Sort in ascending order
          } else if (sortOrder === 'desc') {
              return titleB.localeCompare(titleA, 'en', { numeric: true }); // Sort in descending order
          }
      });
  
      // Clear the movies container
      moviesContainer.innerHTML = '';
  
      // Append the sorted movie elements back to the container
      movieElements.forEach(movieElement => {
          moviesContainer.appendChild(movieElement);
      });
  });
  
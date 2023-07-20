/* Lesson 5 */

/* IF/ELSE IF */

// Step 1: Declare and initialize a new variable to hold the current date
var aboutToday = new Date;
// Step 2: Declare another variable to hold the day of the week
var dayOfTheWeek;
// Step 3: Using the variable declared in Step 1, assign the value of the variable declared in Step 2 to the day of the week ( hint: getDay() )
dayOfTheWeek = aboutToday.getDay();
// Step 4: Declare a variable to hold a message that will be displayed
var aMessage = "";

// Step 5: Using an if statement, if the day of the week is a weekday (i.e. Monday - Friday), set the message variable to the string 'Hang in there!'
// Step 6: Using an else statement, set the message variable to 'Woohoo!  It is the weekend!'
if (dayOfTheWeek > 0 && dayOfTheWeek < 6) {
    aMessage = 'Hang in there!';
} else {
    aMessage = 'Woohoo! It is the weekend!';
}


/* SWITCH, CASE, BREAK */

// Step 1: Declare a new variable to hold another message
var anotherMessage = "";

// Step 2: Use switch, case and break to set the message variable to the day of the week as a string (e.g. Sunday, Monday, etc.) using the day of week variable declared in Step 2 above
switch (dayOfTheWeek) {
    case 0:
        anotherMessage = 'Sunday';
        break;
    case 1:
        anotherMessage = 'Monday';
        break;
    case 2:
        anotherMessage = 'Tuesday';
        break;
    case 3:    
        anotherMessage = 'Wednesday';
        break;
    case 4:    
        anotherMessage = 'Thursday';
        break;
    case 5:    
        anotherMessage = 'Friday';
        break;
    default:
        anotherMessage = 'Saturday'
        break;
}

/* OUTPUT */

// Step 1: Assign the value of the first message variable to the HTML element with an ID of message1
document.getElementById("message1").innerHTML = aMessage;

// Step 2: Assign the value of the second message variable to the HTML element with an ID of message2
document.getElementById("message2").innerHTML = anotherMessage;

/* FETCH */

// Step 1: Declare a global empty array variable to store a list of temples
var templeList = [];

// Step 2: Declare a function named output that accepts a list of temples as an array argument and does the following for each temple:
// - Creates an HTML <article> element
// - Creates an HTML <h3> element and add the temple's templeName property to it
// - Creates an HTML <h4> element and add the temple's location property to it
// - Creates an HTML <h4> element and add the temple's dedicated property to it
// - Creates an HTML <img> element and add the temple's imageUrl property to the src attribute and the temple's templeName property to the alt attribute
// - Appends the <h3> element, the two <h4> elements, and the <img> element to the <article> element as children
// - Appends the <article> element to the HTML element with an ID of temples
function output(temples, filterMonth, sortOrder) {
    let tempId = document.getElementById("temples");
    temples.forEach(element => {
        // Check if the filterMonth is provided and if the temple is dedicated in that month
        if (!filterMonth || (filterMonth && element.dedicated.includes(filterMonth))) {
            // Create the elements for the temple
            let article = document.createElement("article");
            let tempName = document.createElement("h3");
            tempName.innerHTML = element.templeName;
            let tempLoc = document.createElement("h4");
            tempLoc.innerHTML = element.location;
            let tempDed = document.createElement("h4");
            tempDed.innerHTML = element.dedicated;
            let tempImg = document.createElement("img");
            tempImg.setAttribute("src", element.imageUrl);
            tempImg.setAttribute("alt", element.templeName);
            article.appendChild(tempName);
            article.appendChild(tempLoc);
            article.appendChild(tempDed);
            article.appendChild(tempImg);
            tempId.appendChild(article);
        }
    });

    // Sort the temples based on the sorting order
    if (sortOrder === 'yearDedicatedAscending') {
        temples.sort((a, b) => a.dedicated.localeCompare(b.dedicated));
    } else if (sortOrder === 'yearDedicatedDescending') {
        temples.sort((a, b) => b.dedicated.localeCompare(a.dedicated));
    }
}

// Step 3: Create another function called getTemples. Make it an async function.
// Step 4: In the function, using the built-in fetch method, call this absolute URL: 'https://byui-cse.github.io/cse121b-course/week05/temples.json'. Create a variable to hold the response from your fetch. You should have the program wait on this line until it finishes.
// Step 5: Convert your fetch response into a Javascript object ( hint: .json() ). Store this in the templeList variable you declared earlier (Step 1). Make sure the the execution of the code waits here as well until it finishes.
// Step 6: Finally, call the output function and pass it the list of temples. Execute your getTemples function to make sure it works correctly.
async function getTemples () {
    const response = await fetch('https://byui-cse.github.io/cse121b-course/week05/temples.json');

    if (response.ok) {
        templeList = await response.json();
    };

    
    output(templeList);
}

getTemples();

// Step 7: Declare a function named reset that clears all of the <article> elements from the HTML element with an ID of temples
function reset () {
    let resetTemples = document.getElementById('temples');
    resetTemples.innerHTML = "";
}

// Step 8: Declare a function named sortBy that does the following:
// - Calls the reset function
// - Sorts the global temple list by the currently selected value of the HTML element with an ID of sortBy
// - Calls the output function passing in the sorted list of temples
function sortBy() {
    reset();
    let ascDesc = document.getElementById('sortBy');
    let filterMonth = document.getElementById('filterByMonth').value;
    let sortOrder = ascDesc.value;
  
    if (sortOrder === 'templeNameAscending') {
        templeList.sort((a, b) => a.templeName.localeCompare(b.templeName));
    } else if (sortOrder === 'templeNameDescending') {
        templeList.sort((a, b) => b.templeName.localeCompare(a.templeName));
    }
  
    output(templeList, filterMonth, sortOrder);
}

// Step 9: Add a change event listener to the HTML element with an ID of sortBy that calls the sortBy function 
document.getElementById("filterByMonth").addEventListener("change", sortBy);
document.getElementById("sortBy").addEventListener("change", sortBy);

/* STRETCH */

// Consider adding a "Filter by" feature that allows users to filter the list of temples
// This will require changes to both the HTML and the JavaScript files
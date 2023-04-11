// On Mouse Click

function changeCards() {
    let cards = document.getElementsByClassName('card');
    
    for (let i = 0; i < cards.length; i++){ // Ensuring to iterate through the index, as it is using a class meaning there could be multiple
        cards[i].style.backgroundColor = "red"; // Printing it to the index item that it is currently at. And then changing the background color
    }
}

// The above function changes the color of multiple different divs based on the user clicking the paragraph or a button.

// On Mouse Enter and Leave

function turnPink() {
    let box = document.getElementById('box');
    box.style.backgroundColor = 'lightpink'; // Changing the background color of the box id
}

function turnYellow() {
    let box = document.getElementById('box');
    box.style.backgroundColor = 'yellow';
}

// Both the above functions change the background color of the div container based on an event of the mouse entering or leaving the divs area

// Loading events

// There are many different events that can be triggered when a page has been loaded by using the loading events either in the html or js

document.onload = console.log('The document has loaded'); // As soon as the page is loaded, it will log the message to the console

onload=console.log('Hello world'); // By adding this as an attribute to html elements it will trigger the same result - Ensuring code inside ""

/*
oninput and onchange allow us to do things based on what the user has input or done to interact with the web page
*/

oninput // Is where the user physically enters information such as a username or password
onchange // Is where the user changes the value of the item such as selecting information from a drop down list

// Key inputs

onkeydown="keyPressed(event);" // In HTML document elements calls the function below

function keyPressed(event) {
    let key = document.getElementById('key-info') // Gets the element by the id as there is only one, No need to filter through
    key.innerHTML = event.key; // Prints the key value into the html where the key-info is by using the innerHTML.
}

// Event listeners

box.addEventListener("click", changeBorder); // Box is the variable that gets the element to be affected
box.addEventListener("mouseover", changeBackground); // The event listener takes the event that it is looking for to call the function
box.addEventListener("mouseleave", revertBack); // The function is placed last in the line, but without the need to call using ()
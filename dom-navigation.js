document.getElementById('')
document.getElementsByClassName('')
document.getElementsByName('')
document.getElementsByTagName('p')

/*
All the above lines of code get various different items from the DOM. Each one does exactly what it says. Just by passing the required 
information it will allow modification to the specific element. 
They can all be stored in variable's to be called at anytime for the code to do its thing. Allowing cleaner code
*/

// Tag Name

let pElements = document.getElementsByTagName('p'); // Gets all elements with the tag name and outputs them in an array
console.log(pElements);

let secondH1 = document.getElementsByTagName('h1')[1]; // Gets the second h1 element as of the indexing value
console.log(secondH1);

// Class Name - Same as above, but using the class name instead of the tag name

let mainContent = document.getElementsByClassName('main-content');
console.log(mainContent);

let second = document.getElementsByClassName('section-content')[0]; // Displays the first class with that name as of the indexing value
console.log(second);

// Nested elements the family tree of the DOM

let mainDiv = document.getElementById('main-div');  // First get the div itself

let parent = mainDiv.parentNode;  // the div's parent element
let children = mainDiv.children;  // the div's children
let firstChild = mainDiv.children[0];  // the div's first child
let nextSibling = mainDiv.nextElementSibling;  // the next element at the same nesting level
let prevSibling = mainDiv.previousElementSibling;  // the previous element at the same nesting level

let parentElement = document.getElementsByClassName('section-content')[0].parentNode; // Finds the class name and outputs the sections parent element
console.log(parentElement);

let child = document.getElementById('main').children;
console.log(child);

let sibling = document.getElementsByTagName('h1')[0].nextElementSibling;
console.log(sibling);

// Getting specific element properties

let usernameInput = document.getElementById('username-input');
let inputHtml = usernameInput.outerHTML;

console.log(inputHtml);

let inputPadding = window.getComputedStyle(usernameInput).padding; // Gets the padding properties of the usernameInput. Done by passing the variable and the property being searched for
console.log(inputPadding);

// Document write

function getAnswer() {
    document.write("<h2>Answer:</h2>");  
    document.write("<p>By calling it and passing it the content you would like to write to the document</p>")
  };

/*
Document write is a way of adding new html code and styling to a specific document. As the document.write() replaces all existing html 
on the document. Creating a new page with the information that was provided in the function.
The above code in enabled by using the 'onClick' function, detecting when a user clicks the button, it calls the function to 
replace the html
*/

// Changing Styles 

function turnOff() {
    let turnOff = document.getElementById('switch');
     turnOff.style.backgroundColor = 'red';
     turnOff.innerHTML = "OFF";
 }

 /*
 The above function gets an id of 'switch' and due to the onclick event that happens on the button, it will change the background 
 and it changes the inner html text. By adding in standard html code, anything can br created and put in its place
 */

 // innerHTML 

 function todayReport() {
    let today = document.getElementById('report');
    today.innerHTML = `
        <h4>Today</h4>
        <p>Scattered thunderstorms</p>
        <ul>
            <li>Temp: 29C</li>
            <li>Precipitation: 25%</li>
            <li>Humidity: 58%</li>
            <li>Wind: 16km/h</li>
        </ul>
    `;
}

function tomorrowReport() {
    let tomorrow = document.getElementById('report');
    tomorrow.innerHTML = `
        <h4>Tomorrow</h4>
        <p>Partly cloudy</p>
        <ul>
            <li>Temp: 27C</li>
            <li>Precipitation: 20%</li>
            <li>Humidity: 65%</li>
            <li>Wind: 13km/h</li>
        </ul>
    `;
}

/* 
The above function changes what is displayed based on the button that has been clicked on the web page. Changing the html that is displayed.
Using the innerHTML element we are able to write custom html code inside of javascript and place it anywhere in the html document
where the function is called according to where the 'id' is located. Remembering to place the code inside the backticks `....`
*/
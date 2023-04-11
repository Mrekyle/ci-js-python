/*
Functions are reusable blocks of code in Javascript that can be called anytime to perform a certain task. 
There are built in functions such as console.log()
*/

function helloWorld () {
    console.log('Hello World!')
};

helloWorld(); // Will call the function that logs the string hello world!

// Function parameters

function sayMessage (message) { // The message parameter is essentially a variable that has some kind of data stored, but is undefined. 
    console.log(message); // Calling the variable - The defined parameter 
}

sayMessage('Why hello there.. Long time no see!'); // Passing the variable a string for it to log. Now the variable has that string stored. 
sayMessage(); // Will show undefined, as there is no string to be attached to the variable

function multiply (num1, num2) {
    return num1 * num2; // Returns a value, that can be used later on
}

multiply(3, 4); // Multiplies the 2 numbers together that was given to the function according to its parameters. 
console.log(multiply(3, 4)); // Will log the output to the console

let sum = multiply(3, 6);
console.log(sum) // This block of code stores the return of the function in a variable for later use elsewhere

// Math Functions

var maxNumber = Math.max(7, 4, 8, 11, 5, 2); // Math.max outputs the highest number from the data it is given
console.log(maxNumber);

var randomNumber = Math.floor(Math.random() * maxNumber); // Finds the lowest of the data, generates a random number between 0 and 1 and multiplies it by the max number of the given data
console.log(randomNumber)

// Date

Date.now // Outputs the current date of the time that it is called.

// There are many different variations of the built in date Object allowing us to make use of dates and times for different things

let today = 1597673635658;

let date = new Date(today);

let day = date.getDate(); // Uses the date variable to find the day of the specific date today variable. By using the date function 
let month = date.getMonth();
let year = date.getFullYear();

console.log(day);
console.log(month);
console.log(year);
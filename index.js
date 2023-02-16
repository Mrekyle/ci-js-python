let num1 = 5 * (7 - 6);
console.log(num1)

let bool = typeof(true)
console.log(bool)

let num = 5 == 5;
console.log(num);

let string = "Hello world.";
console.log(string)

// Simple multiplication function

let a = 10;
let b = 69;

function multiply() {
    let sum = a * b;
    return sum;
}

sum = multiply()
console.log(sum)

// Simple comparrison 

let numFifty = 50;
let numDecimal = 50.00;
console.log(numFifty === numDecimal);

// If Else Statements 

let h = 10;
let k = 20;
let result;

// If else statments only need to take one condition as it is the same scope level and the same statment. 
if (h < k) {
    result = "a is smaller";
} else {
    result = "a is not smaller";
}

console.log(result);

// If else statments can be chanined together resulting in nested chained if else statments, allowing multiple conditional statments

// If else If else statments - Chaining them together with them selves. 

var age = 15;
var drink 

if (age > 21) {
    drink = "drink whiskey";
} else if (age >= 18) {
    drink = "drink beer";
} else if (age >= 12) {
    drink = "drink cola";
} else {
    drink = "drink apple juice";
}

console.log(drink);

// Nested if else if else statments 
// Based on the two variables it logs a certain string. And if nothing matches it will log the final else statment. 

let user = true;
let emailVerified = false;

if (user === true) {
    if (emailVerified === true) {
        console.log("Welcome to our web-site")
    } else {
        console.log("Please verify your email")
    }
} else {
    console.log("You need to be a user to visit this page")
}

// Dependent of the age variable, it will change the log output to the console. Based on the if else statments. 

//Ternary Expressions

let f = 10;
let d = 20;
let output;

// Write your code below this line. 

result = (f > d) ? "f is smaller" : "f is not smaller"; 
// Compares the two variables together and based on the date logs one of the other strings. 

console.log(output);

// Switch case statments
// Changes the output dependent of the varibles data. If it matches it outputs that specific data match 

let chocolate = ''; 
let errorType = "page";

switch (errorType) {
    case "username":
        chocolate = "That username is incorrect, please try again.";
        break; // Important to break after every statment, as if it matches it will stop the code and output the correct data
    case "password":
        chocolate = "Incorrect password, please try again.";
        break;
    case "page": // The case is what it is searching for in it matching process to find the correct output needed. 
        chocolate = "Sorry this page doesn't exist.";
        break;
    default: // If nothing matches it will output the defualt message
        chocolate = "Error message unknown";
}

console.log(chocolate);



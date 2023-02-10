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

// If Else Statments 

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

//Ternary Expressions

let a = 10;
let b = 20;
let result;

// Write your code below this line. 

result = (a > b) ? "a is smaller" : "a is not smaller"; 
// Compares the two variables together and based on the date logs one of the other strings. 

console.log(result);


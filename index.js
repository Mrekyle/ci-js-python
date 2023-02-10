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

// Write your if statement here:
// If else statments only need to take one condition as it is the same scope level and the same statment. 
if (h < k) {
    result = "a is smaller";
} else {
    result = "a is not smaller";
}

console.log(result);

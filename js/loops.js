// For Loops

let numbers = [42, 65, 0, 9, 73, 10, 11, 44]; // Array for loop to loop through

// Write your code here
for (let i = 0; i < numbers.length; i++) { // .length is important to ensure that the entire length of the array is looped.
    console.log(numbers[i] + 10); // Logging the array with the addition of 10 to each number value.
}

// While Loops

let x = 0;
while (x <= 10) { // Loops through x as long as x is less than 10
	console.log(x);
	x += 1; // In the loop it adds one to x until it hits 10 and then the loop terminates
}

// Do While Loops
// Do while loops always ensure the 'do' expression is always executed no matter what. 

var attemptedUploads = 0

do {
    console.log("Attempting upload...");
    attemptedUploads++; // Adding '1' to the attemptedUploads variable
} while (attemptedUploads < 5);
    console.log("Upload attempts exceeded maximum"); // Logs this string once the variable is equal to 5


// Continue and Break Statements 

for (let i = 0; i <= 20; i++) {
    if (i % 2 !== 0) { // Determines if the output is an even number, if it is it will continue to log the output
        continue; // The continue statements allows the loop to continue as long as the output is an even number until it matches the secondary statement 
    }
    if (i === 10){ // When 'i' i 10 it terminates the loop with the break statement
        break;
    }
    console.log(i) // Console logging inside the loop means that it is in the correct scope plane
    
} 

// Nested Loops - Nesting loops inside of other loops

for(let x = 0; x <= 3; x++) {
	for(let y = 200; y <= 203; y++) {
	  console.log('Outer loop x:',x,'Inner loop y:', y);
	}
  }
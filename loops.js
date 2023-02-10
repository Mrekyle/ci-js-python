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
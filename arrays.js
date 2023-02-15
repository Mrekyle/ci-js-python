// Simple indexing. Arrays index starts at '0' being the first item in the array.

let clothes = ["shirt", "shoes", "socks", "hat", "vest", "shorts", "skirt", "scarf"];

// Write your code here

var varOne = clothes[0]; // Logs the first item as the indexing starts at '0'
console.log(varOne);
var varTwo = clothes[5];
console.log(varTwo)
var varThree = clothes[4];
console.log(varThree);

// Popping removes an element off the end of an array pop()
// Pushing adds an element to the end of an array push()

// Shift removes an element from the beginning of a array shift()
// Unshift adds an element to the beginning of an array unshift()

// Delete will remove any element from the array and replace it as undefined as long as the index is defined delete(5)
// Splicing will remove and delete an element from the array with a defined index splice(3, 1)
// Using splice you can also add elements to an array after defining what to remove and add splice(3, 1, 'Apple', 'Pear')
// The first number states what is desired to be deleted, the second defines how many items after that are deleted and the strings say what to add
// If items are wanted to be added and not deleted, define 0 instead of how many to be deleted. Items will then be added to the array at the point of the defining index

// Changing the original element data is done by hello[3] = 'Banana' - Says that the string called hello with the index of 3 should be replaced with Banana

// Slice allows us to sort and get a specific set of elements from an array slice(2, 4) will get items 2 and 3 from the array
// Allowing us to add this data into a new variable to be called and used somewhere else

// Sorting will sort the array is numerical or alphabetical order depending on the data that is in the array sort()

// Concat allows us to merge 2 or more arrays together and store the new array in a variable hello.concat(chocolate) 
// Useful for needing the arrays separate but also needing the, together in once instance

// Includes checks if an array contains a specific element hello.includes('apples') Will check if the array 'hello' includes apples as part of its array
// Which returns a true of false value

// Simple array functions and operations

let crew = ["Jean-Luc", "Wesley", "Warf", "William", "Data", "Tasha"];
console.log(crew);

// Write your code here

var lastCrewMember = crew.pop(); 
console.log(lastCrewMember);
console.log(crew);
crew.sort();
console.log(crew);
var newCrew = crew.slice(1, 4, 5);
console.log(newCrew);
newCrew.push('Guinan');
console.log(newCrew)
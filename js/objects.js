// Objects is essentially everything. Such as a car. Its a data structure that stores multiple pieces of information
// based on different properties 

let car = {
    price: '500',
    color: 'white',
    engineSize: '5cc',
}

console.log(car.color);

// Accessing information in the object is done like the above. Allowing us to find specific information

// Getting specific objects data and adding new data to the object

let data = {
    firstName: "Arthur",
    lastName: "Dent",
    species: "Human"
};

// add your code here

var firstName = data['firstName']; // Adding the firstName data to a variable of firstName using bracket notation
console.log(firstName);
var species = data.species // Adding the species data to a variable of species using '.' notation
console.log(species);
data.age = 42; // Adding an age to the object
data['firstName'] = 'Kylie'; // Will update the object data's firstName key with a new entry OR
data.firstName = 'Kylie';

console.log(Object.keys(data));
console.log(Object.values(data));
console.log(Object.entries(data));

// Object keys will return the keys of the defined object in a string console.log(Object.Keys(data)) 
// Object Values will return the values of the keys of the defined object a a string console.log(Object.Values(data)) 
// Object Entries will return the key and the value of the defined object in a string console.log(Object.Entries(data))
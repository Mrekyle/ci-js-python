// This keyword always referer's to the current object is connected too. Either in the local scope or in the global scope. Allowing us to access certain
// Data or functions inside objects. 'this' always referer's to what is is defined on

this; 

// The most common way to use this is when using javascript to modify html elements. Such as change the style of a button when it has been pressed

let classroom = {
    numOfStudents: 0,
    schoolHours: false,
    playtime: false,
    openSchool: function() {
        this.schoolHours = true; // Referer's to the schoolHours key inside its parent object. Due to the 'this' keyword
        this.numOfStudents = 20;
    },
    breakTime: function() {
        if(this.schoolHours) { // Using the 'if' keyword, checking if it is true, allowing the playtime to then be set to true
            this.playtime = true;
        }
    }
};

classroom.openSchool(); // Calling this changes the school hours to true
console.log(classroom.numOfStudents) // As long as the school hours is true, the number of students will be set to 20
classroom.breakTime(); // Checks is the school hours are true to set playtime to true
console.log(classroom.playtime)
 

// Iterating Data structures

// The most basic way, setting i as the index and printing out each array item until 'i' is the same as the final item

let chocolate = ['pizza', 'steak', 'pasta', 'fruit salad', 'stir fry'];

for (let i = 0; i < chocolate.length; i++) { // Using the i++ means it is adding 1 to each iteration to log the next item in the array
  console.log(chocolate[i]);
}

// for of loop

let food = ['pizza', 'steak', 'pasta', 'fruit salad', 'stir fry'];
for (let i of food) { // The 'i' represents the index of the food array allowing the array to be iterated through with the loop
  console.log(i);
}

// for in loop - Array

let hello = ['pizza', 'steak', 'pasta', 'fruit salad', 'stir fry'];
for (let i in hello) { // Essentially the same as the for of loop, just using a different keyword.
  console.log('index', i, 'is', hello[i]); // By adding strings together we can add in custom text to the log too.
}

// for in loop - Object

let petNames = {
    dog: 'Fido',
    cat: 'Max',
    fish: 'Bubbles',
    python: 'Mr. Slithers',
  }
  
  for (let i in petNames){
    console.log(petNames[i], 'is a', i); // Allows us to log out the values of the keys using the for in loop
  }

  let gamerScores = {
    john: 89,
    paul: 725,
    george: 553,
    robert: 9302,
    steve: 733,
};
// write your code here

for (let i in gamerScores) {
    console.log(i, 'scored', gamerScores[i]); // First i has no brackets as it referer's to the key, second has brackets as it refer's to the value
}

// Arrays can be nested inside of objects defined by their opening and closing brackets, making it easy to read 
// [] Arrays {} Objects

let company = { // An object with 3 different objects nested inside
    name: 'Apple, Inc',
    founded: 1976,
    financials: { // An object nested inside its parent with an object nested inside itself
      incomeStatement: {
        years: [2020, 2019, 2018], // And array nested inside an object
        revenue: [125, 120, 115],
        costs: [100, 100, 100],
        profit: [25, 20, 15]
      },
      balanceSheet: {
        years: [2020, 2019, 2018],
        assets: [200, 190, 180],
        liabilties: [100, 95, 90],
        equity: [100, 95, 90]
      },
      cashFlow: {
        years: [2020, 2019, 2018],
        operating: [75, 65, 55],
        investing: [22, 20, 18],
        financing: [-94, -80, -75]    
      }
    },
    competitors: ['Microsoft', 'Amazon', 'Samsung']
  }
  
  console.log(company.name);
  console.log(company.competitors);
  console.log(company.competitors[0]);
  console.log(company.financials.incomeStatement.years); // Logs out the years from the financial income statement. Using '.' notation
  console.log(company.financials.incomeStatement.revenue[0]);

var studentData = [ // An Array with two nested objects with nested arrays inside of the objects
    {
        name: 'John Smith',
        email: 'john@gmail.com',
        subjects: ['Math', 'Psychology', 'Physics', 'Chemistry', 'Biology']
    },
    {
        name: 'Mary Jones',
        email: 'mary@gmail.com',
        subjects: ['Fine Art', 'Music', 'Biology', 'Geography', 'Politics']
    }
];

console.log(studentData);
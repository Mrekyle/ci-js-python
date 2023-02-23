/*
Using JS to work with forms allows them to be way more interactive for both sides, the developer and the user
*/

let user = document.getElementById('username'); // Gets the username info from the form by using the id attached to the input element 
let pass = document.getElementById('password');

// Now you can get their values

console.log(user.value); // Prints out the usernames value that was entered into the username field on the form 
console.log(pass.value);

// Preventing default form action

event.preventDefault(); // Takes the event and prevents the default action of the forms as a built in function

/*
Just as we can get data from the forms we can also populate forms using similar methods. Such as when a user fills out there username in a form
the form can auto fill out other information like their name and email. To make things easier and quicker for the user
*/

let userName = document.getElementById('username');
userName.value = 'Kyle Chart' // When the page loads, it will add this strings name into the form username input. 
// Or once the username has been filled out we can find that users other information in a database and insert it in the relevant places

/*
There are three ways to handle form submissions 
the onsubmit="" attribute to be used to call a function
the 'name' method which calls a function by using the name of the form to call the function by getting the id
and by using the name.submit() pre built function inside of a function 
*/

/*
POST and GET Methods
Post send the information from the form in a private way to the database that was specified.
GET requests information from a database to be used in the form. But can risk sensitive data being leaked in the url
Forms will always default to GET unless specified with in the form elements itself or if the default is prevented in JS
*/

/*
Form validation is another important part of working with forms. As it allows us to validate users information, such as when logging into 
a website. Or when registering for a website. This is done by using the important comparison '!==' ensuring that all the data is matched together
Whilst it is possible to do it in html using different attributes. Using JS gives us more control over what happens 
*/

// Basic password validation 

function handleSubmit(event) {
    event.preventDefault();
    let p1 = form.elements['password'].value; // Getting the password data from the input fields and setting them to a variable 
    let p2 = form.elements['confirm-password'].value;
  
    if (p1 !== p2) { // Important comparison used to ensure they are exactly the same 
      let errorDiv = document.getElementById('errors'); // If they don't match it will input the html into the errors div on the html document
      errorDiv.innerHTML = "<p>Please ensure your passwords match.</p>"
    } else {
      console.log('Validation successful!'); // As long as they both match, it will submit the form and anything else that is required.
      form.submit();
    }
  }
  
  let form = document.getElementById('registration-form');
  form.addEventListener('submit', handleSubmit);


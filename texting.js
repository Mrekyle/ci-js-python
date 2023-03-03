let object = {
    name: 'Kyle',
    lName: 'chart',
    girlfriend: 'jess'
}

console.log(object.girlfriend); // Logging items in an array

let myObj = [{
    name: 'hello',
    lName: 'hcnel'
},{
    name: 'hello1',
    girlfriend: 'jess'
},{
    name: 'heh',
    girlfriend: 'holly'
}]

myObj[0].age = 27; // passes the new age value into the object with the index value 0 meaning the first item in the object 
console.log(myObj[0].age) // logging specific items inside nested arrays

let num1 = 54;
let num2 = 4;

function multiply () {
    let answer = num1 * num2;
    return answer;
}

let multiple = multiply() 
console.log(multiple);
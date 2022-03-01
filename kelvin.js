// The code below stores the value of 293 into a constant variable called kelvin
const kelvin = 345;
// The code below converts kelvin to celsius by subtracting 273 from kelvin
const celsius = kelvin - 273;
// The line of code below converts celsius into fahrenheit
let fahrenheit = celsius * (9/5) + 32;
// The line of code below uses the math.floor method to round up temp in fahrenheit with decimal to the nearest whole number.
fahrenheit = Math.floor(fahrenheit);
console.log(`The temperature is ${fahrenheit} degrees fahrenheit`);
console.log(`${kelvin} Kelvin is about ${fahrenheit} degrees Fahrenheit.`);
console.log(`${kelvin} Kelvin is about ${celsius} degrees Celsius.`);
// convert Celsius to Newton
let newton = celsius * (33 / 100);
// round down using math.floor method
newton = Math.floor(newton);
// print the value of newton to the console
console.log(`The temperature is ${newton} degrees Newton`);
// kelvin's value in newton
console.log(`${kelvin} Kelvin is about ${newton} degrees Newton.`)
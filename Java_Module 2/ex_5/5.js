 let numbers=[];
 let number;
 while (true) {
    number = prompt("Enter a number :");
    let number1 = parseInt(number);

    if (numbers.includes(number1)) {
        console.log('The number has already been given');
        break;
    }
    numbers.push(number1);
}
 numbers.sort((a, b)=>(b-a));
 console.log(numbers);
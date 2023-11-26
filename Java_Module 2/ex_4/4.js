 let numbers=[];
 let number = parseInt(prompt("print Number:"));
while(number!==0){
        numbers.push(number);
        number = parseInt(prompt("print Number:"));
    }
    numbers.sort((a, b)=>(b-a))
    console.log(numbers);
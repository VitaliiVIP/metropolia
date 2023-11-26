 let numbers = [];
    const count = 5;
    for (let i = 0; i < count; i++) {
        let input = parseFloat(prompt("Enter a number:"));
            numbers.push(input);
    }
    console.log(numbers);
    for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i])}
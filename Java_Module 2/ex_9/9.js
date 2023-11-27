function even(array){
    let result=0;
    numbers1=[]
    for(let i=0; i<array.length; i++){
        if(array[i]%2===0){
            numbers1.push(array[i])
        }
    }
    return(result)
}
const numbers=[4, 8, 15, 16, 23, 42];
console.log(numbers)
console.log(numbers1)

let rolls=[];
let number = parseInt(prompt("Enter number of sides:"))
let result;
function dice(){
     result = Math.floor(Math.random()*number)+1;
}
while(result!==number){
    dice();
    rolls.push(result);
}
document.write('<ul>');
for (let i = 0; i < rolls.length; i++) {
    document.write('<li>' + rolls[i] + '</li>');
}
document.write('</ul>');
let rolls=[];
let result;
function dice(){
     result = Math.floor(Math.random()*6)+1;
}
while(result!==6){
    dice();
    rolls.push(result);
}
document.write('<ul>');
for (let i = 0; i < rolls.length; i++) {
    document.write('<li>' + rolls[i] + '</li>');
}
document.write('</ul>');
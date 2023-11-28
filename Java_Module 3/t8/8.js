document.getElementById('start').addEventListener('click', calculate);
function calculate(){
const num1 = parseInt(document.getElementById("num1").value);
const num2 = parseInt(document.getElementById("num2").value);
const operation = document.getElementById('operation').value;
let resultParagraph = document.getElementById('result');
let result;
 switch (operation) {
      case 'add':
        result = num1 + num2;
        break;
}
switch (operation) {
      case 'sub':
        result = num1 - num2;
        break;
}
switch (operation) {
      case 'multi':
        result = num1 * num2;
        break;
}
switch (operation) {
      case 'div':
        result = num1 / num2;
        break;
}
resultParagraph.textContent = `Result: ${result}`;
}


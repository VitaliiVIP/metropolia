'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
let target=document.getElementById('target');
for(let i=0; i<students.length; i++){
  let list = document.createElement('option');
  list.value=students[i].id;
  list.textContent=students[i].name;
  target.appendChild(list);
}
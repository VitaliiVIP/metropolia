'use strict';
const names = ['John', 'Paul', 'Jones'];
let target = document.getElementById('target');
let html = '';
for(let i=0; i<names.length; i++){
    html += '<li>'+names[i]+ '</li>';
}
target.innerHTML=html;
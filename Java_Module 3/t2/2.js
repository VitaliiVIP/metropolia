let target = document.getElementById('target');
let list = document.createElement('ul');
let item1 = document.createElement('li');
item1.textContent = 'First item';
list.appendChild(item1);

let item2 = document.createElement('li');
item2.textContent = 'Second item';
list.appendChild(item2);

let item3 = document.createElement('li');
item3.textContent = 'Third item';
list.appendChild(item3);
target.classList.add('my-list');
target.appendChild(list)
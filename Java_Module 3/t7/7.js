const target = document.getElementById('target');
const trigger = document.getElementById('trigger');
trigger.addEventListener('mouseover', ()=>{
    target.src="picA.jpg";
});
target.addEventListener('mouseout', ()=>{
    target.src="picB.jpg";
});

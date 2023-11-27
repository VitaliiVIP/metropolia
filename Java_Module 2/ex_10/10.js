const quantity=parseInt(prompt("Enter the number of candidates"))
let cand=[];

for(let i=0; i<quantity; i++){
    let name=prompt("Enter the name");
    let vote=parseInt(prompt("Enter how much votes got"));
    cand.push({ names: name, votes: vote });
}

let win = cand[0]; // Assume the first candidate is the winner
for (let i = 1; i < quantity; i++) {
    if (cand[i].votes > win.votes) {
        win = cand[i];
    }
}

console.log("The winner is " + win.names + " with " + win.votes + " votes.");
console.log("results:");
for(let i=0; i<quantity; i++){
    console.log(cand[i].names +": "+ cand[i].votes);
}

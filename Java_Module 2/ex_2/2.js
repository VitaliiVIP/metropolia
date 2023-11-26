const count = parseInt(prompt("Enter quantity of numbers:"));
        const participants = [];

        for (let i = 1; i <= count; i++) {
            const name = prompt(`Enter name ${i}:`);
            participants.push(name);
        }

        participants.sort();

        const ol = document.createElement("ol");
        participants.forEach(name => {
            const text = document.createElement("li");
            text.textContent = name;
            ol.appendChild(text);
        });

        document.body.appendChild(ol);
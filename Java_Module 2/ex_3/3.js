const count = 6;
            const participants = [];

            for (let i = 1; i <= count; i++) {
                const name = prompt(`Enter name ${i}:`);
                participants.push(name);
            }

            participants.sort();
            participants.reverse()

            const ul = document.createElement("ul");
            participants.forEach(name => {
                const text = document.createElement("li");
                text.textContent = name;
                ul.appendChild(text);
            });

            document.body.appendChild(ul);

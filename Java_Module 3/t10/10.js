document.getElementById('source').addEventListener('submit', function (event) {
    event.preventDefault();

    const fn = document.getElementById('firstname').value;
    const ln = document.getElementById('lastname').value;
    const target = document.getElementById('target');
    target.textContent = '${fn} ${ln}';
});
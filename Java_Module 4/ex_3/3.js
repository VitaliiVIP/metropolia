document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('search');
    const results = document.getElementById('results');
    const handleSubmit = async function (event) {
        event.preventDefault();
        const query = document.getElementById('query').value;

        try {
            const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
            const data = await response.json();
            displayResultsOnPage(data);
            resconsole(data);
            form.removeEventListener('submit', handleSubmit);
        } catch (error) {
            console.error('Error:', error.message);
        }
    };
    function resconsole(data) {
        console.log( data);
    }

    form.addEventListener('submit', handleSubmit);
    function displayResultsOnPage(data) {
        results.innerHTML = '';
        data.forEach(show => {
            const article = document.createElement('article');
            const name = document.createElement('h2');
            name.textContent = show.show.name;
            const img = document.createElement('img');
            img.src = show.show.image.medium;
            img.alt = show.show.name;
            const url = document.createElement('a');
            url.href = show.show.url;
            url.textContent = 'Details';
            const summary = document.createElement('div');
            summary.innerHTML = show.show.summary;
            article.appendChild(name);
            article.appendChild(img);
            article.appendChild(url);
            article.appendChild(summary);
            results.appendChild(article);
        });
    }
});

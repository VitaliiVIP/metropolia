document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('search');
    const handleSubmit = async function (event) {
        event.preventDefault();
        const query = document.getElementById('query').value;
        try {
            const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
            const data = await response.json();
            resconsole(data);
            form.removeEventListener('submit', handleSubmit);
        } catch (error) {
            console.error('Error:', error.message);
        }
    };
    form.addEventListener('submit', handleSubmit);
    function resconsole(data) {
        console.log( data);
    }
});

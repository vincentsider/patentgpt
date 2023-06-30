document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    const resultsTable = document.getElementById('resultsTable');
    const costEstimate = document.getElementById('costEstimate');
    const errorMessage = document.getElementById('errorMessage');

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(searchForm);
        fetch('/search', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                resultsTable.innerHTML = data.results;
                costEstimate.innerHTML = data.estimate;
                errorMessage.style.display = 'none';
            } else {
                errorMessage.innerHTML = data.message;
                errorMessage.style.display = 'block';
            }
        })
        .catch(error => {
            errorMessage.innerHTML = 'An error occurred. Please try again.';
            errorMessage.style.display = 'block';
        });
    });
});
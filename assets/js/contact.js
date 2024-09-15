document.querySelector('.php-email-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const form = event.target;
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector('.sent-message').style.display = 'block';
        document.querySelector('.error-message').style.display = 'none';
    })
    .catch(error => {
        document.querySelector('.sent-message').style.display = 'none';
        document.querySelector('.error-message').style.display = 'block';
        console.error('Error:', error);
    });
});

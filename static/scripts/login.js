document.getElementById('login-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/auth/api-login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({username, password})
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem('access', data.access);
        localStorage.setItem('refresh', data.refresh);
        document.getElementById('message').innerText = 'Login successful!';
        window.location.href = 'home';  // Redirect to homepage or dashboard
    } else {
        document.getElementById('message').innerText = data.error || 'Login failed';
    }
});
const loginForm = document.getElementById('login-form');
const logoutSection = document.getElementById('logout-section');
const loginMessage = document.getElementById('login-message');
const loggedInUser = document.getElementById('logged-in-user');
const logoutMessage = document.getElementById('logout-message');

// Function to handle login
async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/auth/api-login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({username, password}),
        });

        const data = await response.json();

        if (response.ok) {
            // Login successful
            loginMessage.textContent = 'Login successful!';
            loginMessage.className = 'message';
            loginForm.style.display = 'none';
            logoutSection.style.display = 'block';
            loggedInUser.textContent = username;
        } else {
            // Login failed
            loginMessage.textContent = data.error || 'Login failed. Please try again.';
            loginMessage.className = 'message error';
        }
    } catch (error) {
        loginMessage.textContent = 'An error occurred. Please try again.';
        loginMessage.className = 'message error';
    }
}



// Function to handle logout
async function logout() {
    try {
        const response = await fetch('http://127.0.0.1:8000/auth/api-logout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        const data = await response.json();

        if (response.ok) {
            // Logout successful
            logoutMessage.textContent = 'Logout successful!';
            logoutMessage.className = 'message';
            logoutSection.style.display = 'none';
            loginForm.style.display = 'block';
        } else {
            // Logout failed
            logoutMessage.textContent = data.error || 'Logout failed. Please try again.';
            logoutMessage.className = 'message error';
        }
    } catch (error) {
        logoutMessage.textContent = 'An error occurred. Please try again.';
        logoutMessage.className = 'message error';
    }
}
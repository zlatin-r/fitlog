document.addEventListener('DOMContentLoaded', function () {
    const logoutLink = document.getElementById('logout-link');

    if (logoutLink) {
        logoutLink.addEventListener('click', async (event) => {
            event.preventDefault();  // Prevent the default link behavior

            try {
                // Clear tokens from localStorage
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');

                // Redirect to the home page
                window.location.href = '/';  // Replace with your home page URL
            } catch (error) {
                console.error('Error during logout:', error);
            }
        });
    } else {
        console.error('Logout link not found');
    }
});
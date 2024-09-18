document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'admin' && password === 'pas') {
        alert('Login successful!');
    } else {
        document.getElementById('errorMessage').textContent = 'Invalid username or password';
    }
});

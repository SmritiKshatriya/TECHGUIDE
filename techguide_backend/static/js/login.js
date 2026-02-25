/* ============================================================
   TECHGUIDE — LOGIN JAVASCRIPT
============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  // Already logged in? Go home
  if (localStorage.getItem('tg-user')) {
    window.location.href = '/';
    return;
  }

  document.getElementById('login-form').addEventListener('submit', handleLogin);
});

async function handleLogin(e) {
  e.preventDefault();

  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value;
  const errorEl  = document.getElementById('login-error');
  const btn      = document.getElementById('login-btn');

  errorEl.classList.remove('visible');

  if (!username || !password) {
    errorEl.textContent = 'Please fill in all fields.';
    errorEl.classList.add('visible');
    return;
  }

  btn.disabled = true;
  btn.textContent = 'Logging in…';

  try {
    const res = await fetch('/api/accounts/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken()
      },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem('tg-user', JSON.stringify(data.user));
      const redirect = localStorage.getItem('tg-redirect') || '/';
      localStorage.removeItem('tg-redirect');
      window.location.href = redirect;
    } else {
      errorEl.textContent = data.error || 'Invalid credentials.';
      errorEl.classList.add('visible');
      btn.disabled = false;
      btn.textContent = 'Log In';
    }
  } catch (err) {
    errorEl.textContent = 'Something went wrong. Please try again.';
    errorEl.classList.add('visible');
    btn.disabled = false;
    btn.textContent = 'Log In';
  }
}

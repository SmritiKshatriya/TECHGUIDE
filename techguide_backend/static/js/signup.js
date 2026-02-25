/* ============================================================
   TECHGUIDE — SIGNUP JAVASCRIPT
============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('tg-user')) {
    window.location.href = '/';
    return;
  }

  document.getElementById('signup-form').addEventListener('submit', handleSignup);
});

async function handleSignup(e) {
  e.preventDefault();

  const username        = document.getElementById('username').value.trim();
  const email           = document.getElementById('email').value.trim();
  const password        = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirm-password').value;
  const errorEl         = document.getElementById('signup-error');
  const successEl       = document.getElementById('signup-success');
  const btn             = document.getElementById('signup-btn');

  errorEl.classList.remove('visible');
  successEl.classList.remove('visible');

  if (!username || !email || !password || !confirmPassword) {
    errorEl.textContent = 'Please fill in all fields.';
    errorEl.classList.add('visible');
    return;
  }

  btn.disabled = true;
  btn.textContent = 'Creating account…';

  try {
    const res = await fetch('/api/accounts/signup/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken()
      },
      body: JSON.stringify({ username, email, password, confirm_password: confirmPassword })
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem('tg-user', JSON.stringify(data.user));
      successEl.textContent = 'Account created! Redirecting…';
      successEl.classList.add('visible');
      const redirect = localStorage.getItem('tg-redirect') || '/';
      localStorage.removeItem('tg-redirect');
      setTimeout(() => window.location.href = redirect, 1200);
    } else {
      errorEl.textContent = data.error || 'Something went wrong.';
      errorEl.classList.add('visible');
      btn.disabled = false;
      btn.textContent = 'Create Account';
    }
  } catch (err) {
    errorEl.textContent = 'Something went wrong. Please try again.';
    errorEl.classList.add('visible');
    btn.disabled = false;
    btn.textContent = 'Create Account';
  }
}

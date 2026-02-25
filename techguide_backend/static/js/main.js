/* ============================================================
   TECHGUIDE — SHARED JAVASCRIPT
   Theme toggle · Auth navbar · CSRF · Scroll animations
============================================================ */

/* ── THEME ── */
(function initTheme() {
  const saved = localStorage.getItem('tg-theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  updateToggleIcon(saved);
})();

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('tg-theme', next);
  updateToggleIcon(next);
}

function updateToggleIcon(theme) {
  const btn = document.getElementById('theme-toggle');
  if (btn) btn.textContent = theme === 'dark' ? '☀️' : '🌙';
}

/* ── CSRF ── */
function getCsrfToken() {
  let value = null;
  if (document.cookie) {
    document.cookie.split(';').forEach(c => {
      c = c.trim();
      if (c.startsWith('csrftoken=')) {
        value = decodeURIComponent(c.substring('csrftoken='.length));
      }
    });
  }
  return value;
}

/* ── AUTH NAVBAR ── */
function renderAuthNav(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const raw = localStorage.getItem('tg-user');
  if (raw) {
    const user = JSON.parse(raw);
    container.innerHTML = `
      <span class="nav-username">Hi, ${user.username} 👋</span>
      <button class="btn btn-outline" onclick="handleLogout()">Log Out</button>
    `;
  } else {
    container.innerHTML = `
      <a href="/login/" class="btn btn-outline">Log In</a>
      <a href="/signup/" class="btn btn-primary">Sign Up</a>
    `;
  }
}

async function handleLogout() {
  try {
    await fetch('/api/accounts/logout/', {
      method: 'POST',
      headers: { 'X-CSRFToken': getCsrfToken() }
    });
  } catch (e) {}
  localStorage.removeItem('tg-user');
  window.location.href = '/';
}

/* ── ACTIVE NAV LINK ── */
function setActiveNavLink() {
  const path = window.location.pathname;
  document.querySelectorAll('.navbar-links a').forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');
    if (href && href !== '/' && path.startsWith(href)) {
      link.classList.add('active');
    } else if (href === '/' && path === '/') {
      link.classList.add('active');
    }
  });
}

/* ── SCROLL ANIMATIONS ── */
function initScrollAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('in-view');
        }, i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.animate-in').forEach(el => observer.observe(el));
}

/* ── TYPEWRITER ── */
function typewriter(elementId, text, speed = 55, onDone) {
  const el = document.getElementById(elementId);
  if (!el) return;
  let i = 0;
  el.textContent = '';
  const cursor = document.createElement('span');
  cursor.className = 'typewriter-cursor';
  el.parentNode.insertBefore(cursor, el.nextSibling);

  const timer = setInterval(() => {
    el.textContent += text[i];
    i++;
    if (i >= text.length) {
      clearInterval(timer);
      cursor.remove();
      if (onDone) onDone();
    }
  }, speed);
}

/* ── INIT ON DOM READY ── */
document.addEventListener('DOMContentLoaded', () => {
  renderAuthNav('auth-nav');
  setActiveNavLink();
  initScrollAnimations();
});

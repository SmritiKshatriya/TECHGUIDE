/* ============================================================
   TECHGUIDE — ROADMAPS LISTING JAVASCRIPT
============================================================ */

async function loadDomains() {
  try {
    const res = await fetch('/api/quiz/domains/');
    const domains = await res.json();
    const grid = document.getElementById('domains-grid');
    grid.innerHTML = '';

    domains.forEach((domain, i) => {
      const card = document.createElement('div');
      card.className = 'domain-card animate-in';
      card.style.transitionDelay = (i * 60) + 'ms';
      card.innerHTML = `
        <div class="emoji">${domain.icon_emoji}</div>
        <h3>${domain.name}</h3>
        <p>${domain.description}</p>
        <a href="/roadmap/?domain=${domain.slug}" class="explore-link"
           style="color:${domain.color_hex}">
          Explore Roadmap →
        </a>
      `;
      card.addEventListener('click', () => {
        window.location.href = '/roadmap/?domain=' + domain.slug;
      });
      grid.appendChild(card);
    });

    if (typeof initScrollAnimations === 'function') initScrollAnimations();

  } catch (err) {
    document.getElementById('domains-grid').innerHTML =
      '<p style="color:var(--error);">Failed to load domains. Please refresh.</p>';
  }
}

document.addEventListener('DOMContentLoaded', loadDomains);

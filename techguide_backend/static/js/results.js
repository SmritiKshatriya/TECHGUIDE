/* ============================================================
   TECHGUIDE — RESULTS JAVASCRIPT
============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  const raw = localStorage.getItem('tg-results');
  if (!raw) {
    window.location.href = '/quiz/';
    return;
  }

  const data = JSON.parse(raw);
  const results = data.results;
  const container = document.getElementById('results-list');
  const ranks = ['🥇 Best Match', '🥈 Second Match', '🥉 Third Match'];

  results.forEach((domain, i) => {
    const card = document.createElement('div');
    card.className = 'result-card';
    card.innerHTML = `
      <div class="result-top">
        <span class="rank-badge">${ranks[i]}</span>
        <span class="compat-pct" style="color:${domain.color_hex}">${domain.compatibility}%</span>
      </div>
      <div class="domain-info">
        <span class="emoji">${domain.icon_emoji}</span>
        <h3>${domain.name}</h3>
      </div>
      <div class="compat-bar-track">
        <div class="compat-bar-fill" style="background:${domain.color_hex}" data-width="${domain.compatibility}"></div>
      </div>
      <a href="/roadmap/?domain=${domain.slug}"
         class="roadmap-link"
         style="color:${domain.color_hex}; border-color:${domain.color_hex}">
        View ${domain.name} Roadmap →
      </a>
    `;
    container.appendChild(card);

    // Animate card in
    setTimeout(() => {
      card.classList.add('visible');
      // Animate bar
      setTimeout(() => {
        const bar = card.querySelector('.compat-bar-fill');
        bar.style.width = bar.dataset.width + '%';
      }, 200);
    }, i * 200);
  });
});

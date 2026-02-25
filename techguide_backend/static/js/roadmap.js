/* ============================================================
   TECHGUIDE — ROADMAP JAVASCRIPT
============================================================ */

const levelNames = {
  1: { label: 'Level 1 — Foundations', emoji: '🌱', time: '0–3 months' },
  2: { label: 'Level 2 — Beginner',    emoji: '🚀', time: '3–6 months' },
  3: { label: 'Level 3 — Intermediate',emoji: '⚡', time: '6–12 months' },
  4: { label: 'Level 4 — Advanced',    emoji: '🔥', time: '12–18 months' },
  5: { label: 'Level 5 — Expert',      emoji: '👑', time: '18+ months' },
};

const resourceIcons = {
  VIDEO:       '▶',
  ARTICLE:     '📄',
  COURSE:      '🎓',
  BOOK:        '📚',
  INTERACTIVE: '⚡',
  PROJECT:     '🔨',
};

async function loadRoadmap() {
  const params = new URLSearchParams(window.location.search);
  const domain = params.get('domain') || 'web-development';

  try {
    const res = await fetch('/api/roadmaps/?domain=' + domain);
    const steps = await res.json();

    if (!steps.length) {
      document.getElementById('roadmap-loading').textContent = 'No roadmap found for this domain yet.';
      return;
    }

    // Set title
    const title = domain.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
    document.getElementById('roadmap-title').textContent = title;
    document.title = title + ' Roadmap — TechGuide';

    // Group by level
    const grouped = {};
    steps.forEach(step => {
      if (!grouped[step.level]) grouped[step.level] = [];
      grouped[step.level].push(step);
    });

    const container = document.getElementById('roadmap-content');
    container.innerHTML = '';

    Object.keys(grouped).sort().forEach(level => {
      const info = levelNames[level] || { label: 'Level ' + level, emoji: '📌', time: '' };

      const section = document.createElement('div');
      section.className = 'level-section animate-in';

      section.innerHTML = `
        <div class="level-heading">
          ${info.emoji} ${info.label}
          <span style="font-size:0.8rem; color:var(--muted); font-weight:500;">${info.time}</span>
        </div>
      `;

      grouped[level].forEach(step => {
        const item = document.createElement('div');
        item.className = 'step-item';

        // Resources HTML
        let resourcesHtml = '';
        if (step.resources && step.resources.length) {
          const chips = step.resources.map(r => `
            <a href="${r.url}" target="_blank" class="resource-chip"
               onclick="event.stopPropagation()">
              <span>${resourceIcons[r.resource_type] || '🔗'}</span>
              <span>${r.title}</span>
              <span class="${r.is_free ? 'free-tag' : 'paid-tag'}">${r.is_free ? 'FREE' : 'PAID'}</span>
            </a>
          `).join('');
          resourcesHtml = `
            <div class="resources-label">Resources</div>
            <div class="resources-list">${chips}</div>
          `;
        } else {
          resourcesHtml = '<p style="font-size:0.85rem; color:var(--muted);">No resources added yet.</p>';
        }

        item.innerHTML = `
          <div class="step-header">
            <div class="step-header-left">
              ${step.is_milestone ? '<span class="milestone-star">⭐</span>' : ''}
              <span class="step-title">${step.title}</span>
            </div>
            <div class="step-meta">
              <span class="step-weeks">${step.estimated_weeks}w</span>
              <span class="step-chevron">▼</span>
            </div>
          </div>
          <div class="step-body">
            <p class="step-desc">${step.description}</p>
            ${resourcesHtml}
          </div>
        `;

        item.querySelector('.step-header').addEventListener('click', () => {
          item.classList.toggle('open');
        });

        section.appendChild(item);
      });

      container.appendChild(section);
    });

    document.getElementById('roadmap-loading').style.display = 'none';
    document.getElementById('roadmap-content').style.display = 'block';

    // Trigger scroll animations
    if (typeof initScrollAnimations === 'function') initScrollAnimations();

  } catch (err) {
    document.getElementById('roadmap-loading').textContent = 'Failed to load roadmap.';
  }
}

document.addEventListener('DOMContentLoaded', loadRoadmap);

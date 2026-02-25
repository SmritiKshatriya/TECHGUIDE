/* ============================================================
   TECHGUIDE — QUIZ JAVASCRIPT
============================================================ */

let questions = [];
let currentIndex = 0;
let answers = {};
let selectedChoiceId = null;

async function loadQuestions() {
  try {
    const res = await fetch('/api/quiz/questions/');
    questions = await res.json();
    document.getElementById('quiz-loading').style.display = 'none';
    document.getElementById('quiz-area').style.display = 'block';
    showQuestion(0);
  } catch (err) {
    document.getElementById('quiz-loading').textContent = 'Failed to load quiz. Please refresh.';
  }
}

function showQuestion(index) {
  const q = questions[index];
  selectedChoiceId = null;

  // Progress
  const pct = (index / questions.length) * 100;
  document.getElementById('progress-fill').style.width = pct + '%';
  document.getElementById('progress-current').textContent = index + 1;
  document.getElementById('progress-total').textContent = questions.length;

  // Question
  document.getElementById('category-tag').textContent = q.category;
  document.getElementById('question-text').textContent = q.question_text;

  // Choices
  const grid = document.getElementById('choices-grid');
  grid.innerHTML = '';
  q.choices.forEach(choice => {
    const btn = document.createElement('button');
    btn.className = 'choice-btn';
    btn.textContent = choice.choice_text;
    btn.dataset.id = choice.id;
    btn.addEventListener('click', () => selectChoice(choice.id, btn));
    grid.appendChild(btn);
  });

  // Restore previous answer if going back
  const prev = answers[String(q.id)];
  if (prev) {
    const prevBtn = grid.querySelector(`[data-id="${prev}"]`);
    if (prevBtn) prevBtn.classList.add('selected');
    selectedChoiceId = parseInt(prev);
    showNextBtn(index);
  } else {
    hideNextBtn();
  }
}

function selectChoice(choiceId, clickedBtn) {
  document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));
  clickedBtn.classList.add('selected');
  selectedChoiceId = choiceId;
  showNextBtn(currentIndex);
}

function showNextBtn(index) {
  const btn = document.getElementById('next-btn');
  btn.textContent = index === questions.length - 1 ? 'See My Results →' : 'Next →';
  btn.classList.add('visible');
}

function hideNextBtn() {
  document.getElementById('next-btn').classList.remove('visible');
}

function nextQuestion() {
  if (!selectedChoiceId) return;

  const q = questions[currentIndex];
  answers[String(q.id)] = String(selectedChoiceId);

  if (currentIndex < questions.length - 1) {
    currentIndex++;
    showQuestion(currentIndex);
  } else {
    submitQuiz();
  }
}

async function submitQuiz() {
  document.getElementById('loading-overlay').classList.add('visible');

  try {
    const res = await fetch('/api/quiz/submit/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken()
      },
      body: JSON.stringify({ answers })
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem('tg-results', JSON.stringify(data));
      window.location.href = '/results/';
    } else {
      throw new Error(data.error || 'Server error');
    }
  } catch (err) {
    document.getElementById('loading-overlay').classList.remove('visible');
    const errBox = document.getElementById('quiz-error');
    errBox.textContent = err.message || 'Something went wrong. Please try again.';
    errBox.classList.add('visible');
  }
}

// Guard: must be logged in
const tgUser = localStorage.getItem('tg-user');
if (!tgUser) {
  localStorage.setItem('tg-redirect', '/quiz/');
  window.location.href = '/login/';
} else {
  document.addEventListener('DOMContentLoaded', loadQuestions);
}

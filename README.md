## TechGuide — Tech Career Guidance Platform

TechGuide is a web application that helps students and aspiring developers discover their ideal tech domain through a guided quiz and personalized learning roadmaps, backed by curated learning resources.

---

## Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: SQLite (default Django configuration)
- **Frontend**: HTML, Tailwind CSS (via CDN), vanilla JavaScript
- **APIs**: JSON APIs built with DRF
- **Other**: `django-cors-headers` for CORS handling

---

## Features

- **Personalized Quiz System**
  - 20-question quiz that captures interests, strengths, and work style.
  - Each answer contributes weighted scores toward multiple tech domains.
  - Returns top-matching domains with compatibility percentages.

- **Domain Roadmaps**
  - Domain model for areas like Web Development, Data Science, Cybersecurity, AI/ML, Mobile, Cloud & DevOps.
  - Structured `RoadmapStep` model with levels (Foundations → Expert), ordering, milestones, and estimated weeks.
  - API endpoint to fetch steps for a given domain, used by the roadmap UI.

- **Resource Library**
  - `Resource` model linked to roadmap steps.
  - Supports different resource types (video, article, course, book, interactive, project), platforms, free/paid, difficulty, estimated hours.
  - Roadmaps can surface curated resources at each step.

- **Modern UI**
  - Dark-themed landing page (`index.html`) with Tailwind CSS.
  - Quiz page (`quiz.html`) that fetches questions from the API and submits answers, with smooth transitions and progress indicators.
  - Results and roadmap pages for visualizing matches and learning paths.

- **Admin Interface**
  - Django admin configured for:
    - Managing quiz questions, choices, and domain scoring.
    - Editing domains, roadmaps, and resources with filters, search, and inlines.

---

## Getting Started (Run Locally)

### Prerequisites

- **Python**: 3.10+ recommended
- **Git**

### Installation & Setup

```bash
# 1. Clone the repo
git clone <your-repo-url> TechGuide
cd TechGuide

# 2. Go into the Django project
cd techguide_backend

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment (Windows)
venv\Scripts\activate

# 5. Install dependencies
pip install django djangorestframework django-cors-headers

# 6. Apply database migrations
python manage.py migrate

# 7. Create a superuser for the admin
python manage.py createsuperuser

# 8. Run the development server
python manage.py runserver
```

Then open:

- `http://127.0.0.1:8000/` → Landing page (TechGuide home)
- `http://127.0.0.1:8000/quiz/` → Quiz UI
- `http://127.0.0.1:8000/results/` → Results page
- `http://127.0.0.1:8000/roadmap/` → Roadmap UI
- `http://127.0.0.1:8000/admin/` → Django admin

---

## API Endpoints

All API endpoints are prefixed with `/api/`.

### Quiz

- **GET `/api/quiz/questions/`**
  - **Description**: Returns all quiz questions with their choices.
  - **Response shape (example)**:

    ```json
    [
      {
        "id": 1,
        "question_text": "You enjoy breaking problems into smaller logical steps.",
        "category": "TECHNICAL",
        "order": 1,
        "choices": [
          { "id": 3, "choice_text": "Strongly agree", "order": 1 },
          { "id": 4, "choice_text": "Agree", "order": 2 }
        ]
      }
    ]
    ```

- **POST `/api/quiz/submit/`**
  - **Description**: Accepts quiz answers and returns top-matching domains with scores.
  - **Request body**:

    ```json
    {
      "answers": {
        "1": "3",
        "2": "7",
        "3": "11",
        "4": "16"
      }
    }
    ```

  - **Keys**: question IDs (as strings).
  - **Values**: selected choice IDs (as strings).

  - **Response body (example)**:

    ```json
    {
      "results": [
        {
          "name": "Web Development",
          "slug": "web-development",
          "icon_emoji": "🌐",
          "color_hex": "#3B82F6",
          "compatibility": 92
        },
        {
          "name": "Data Science",
          "slug": "data-science",
          "icon_emoji": "📊",
          "color_hex": "#22C55E",
          "compatibility": 81
        },
        {
          "name": "AI & Machine Learning",
          "slug": "ai-ml",
          "icon_emoji": "🤖",
          "color_hex": "#A855F7",
          "compatibility": 76
        }
      ]
    }
    ```

### Roadmaps

- **GET `/api/roadmaps/`**
  - **Description**: Returns roadmap steps. Optionally filter by domain slug.
  - **Query params**:
    - `domain` *(optional)* — domain slug (e.g. `web-development`).
  - **Examples**:
    - `/api/roadmaps/` → All roadmap steps for all domains.
    - `/api/roadmaps/?domain=web-development` → Steps only for Web Development.
  - **Response shape (example)**:

    ```json
    [
      {
        "id": 1,
        "domain": "web-development",
        "domain_name": "Web Development",
        "title": "Learn HTML & CSS fundamentals",
        "description": "...",
        "level": 1,
        "level_label": "Foundations",
        "order": 1,
        "estimated_weeks": 2,
        "is_milestone": true
      }
    ]
    ```

> **Note**: Additional endpoints can be documented here if you expose more APIs for resources, domains, or admin-only operations.

---

## Screenshots

_Add screenshots of the main pages once available._

- **Landing Page** — `screenshots/landing.png`
- **Quiz** — `screenshots/quiz.png`
- **Results** — `screenshots/results.png`
- **Roadmap** — `screenshots/roadmap.png`

---

## Author

**Smriti Kshatriya**

Built for students and aspiring developers exploring tech careers. Contributions, suggestions, and feedback are welcome.


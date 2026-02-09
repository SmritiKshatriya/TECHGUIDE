# Tech Guide 🚀

**Tech Guide** is a full-stack web application designed to help students discover their ideal career path in technology. It acts as a personal career counselor by assessing interests through an interactive quiz and providing personalized learning roadmaps with curated resources.

## 🌟 Key Features

*   **Smart Career Discovery:** A dynamic quiz engine that evaluates user interests (Visual vs. Logic vs. Data).
*   **Personalized Recommendations:** automatically suggests a Tech Domain (e.g., Frontend, Backend, Data Science) based on quiz scores.
*   **Dynamic Roadmaps:** Provides step-by-step learning paths specific to the recommended domain.
*   **Curated Resources:** Direct links to high-quality learning materials for every step.
*   **User Accounts:** Full authentication system (Sign Up/Login) to save progress.
*   **Persistent Results:** Users can log out and return later to see their saved career path.
*   **AI Integration:** Includes a Scikit-Learn Machine Learning model to predict career paths (currently in demo mode alongside rule-based logic).

---

## 🛠️ Tech Stack

| Layer | Technology | Usage |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3 | Responsive UI design, Flexbox layouts. |
| **Backend** | Python, Django | MVT Architecture, URL Routing, View Logic. |
| **Database** | SQLite3 | Storing Users, Quiz Questions, Results, and Resources. |
| **Authentication** | Django Auth System | Secure Login, Registration, Session Management. |
| **AI / ML** | Scikit-Learn, Pandas | Decision Tree Classifier for career prediction. |
| **Version Control** | Git & GitHub | Source code management. |

---

## 📂 Project Structure

*   `techguide/` - Main project configuration (Settings, URLs).
*   `quiz/` - The core application handling logic.
    *   `models.py` - Database schemas for Questions, Choices, Domains, and Resources.
    *   `views.py` - Business logic for the quiz, scoring, and user dashboards.
    *   `templates/` - HTML files for Home, Quiz, Result, and Auth pages.
    *   `static/` - CSS and assets.
*   `train_model.py` - Script to train the AI model using sample data.
*   `db.sqlite3` - The local database file.

---

## ⚡ Getting Started

Follow these instructions to run the project locally.

### Prerequisites
*   Python 3.x installed.
*   Git installed.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd TechGuide
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install django scikit-learn pandas joblib
    ```

4.  **Apply Database Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the App:**
    Open your browser and go to `http://127.0.0.1:8000/`

---

## 🔮 Future Roadmap

*   [ ] Advanced AI model trained on real user data.
*   [ ] Categorized resources (Video vs. Articles, Free vs. Paid).
*   [ ] Progress tracking for individual roadmap steps.
*   [ ] Community forum for students.

---

Made with ❤️ using Django.

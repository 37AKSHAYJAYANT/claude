# Spendly — Personal Expense Tracker

> **Track every rupee. Own your finances.**

Spendly is a modern, lightweight personal finance and expense tracking web application built with **Python (Flask)**, **SQLite**, and **HTML5/CSS3/Vanilla JavaScript**. It helps users log daily transactions, categorize spending, analyze spending patterns, and maintain control over their personal budget.

---

## 🚀 Features

- **Modern Landing Page**: Dribbble-inspired hero header with interactive category filters, search keywords, and promo banners.
- **Interactive Video Modal**: Built-in popup video player with clean vanilla JavaScript controls (automatic stop-on-close).
- **Authentication**: Dedicated user registration and sign-in interfaces.
- **Legal & Compliance**: Dedicated, styled **Terms and Conditions** (`/terms`) and **Privacy Policy** (`/privacy`) pages.
- **Expense Tracking API & Routes**: Prepared endpoints for managing expenses (add, edit, delete, categorization, monthly breakdown).
- **Zero Framework Bloat**: Fast-loading UI built entirely with semantic HTML, modern CSS custom properties, and vanilla JS.

---

## 📁 Project Structure

```text
expense-tracker/
├── app.py                     # Main Flask application and route definitions
├── requirements.txt           # Python package dependencies
├── database/
│   ├── __init__.py
│   └── db.py                  # SQLite database connection & schema helpers
├── static/
│   ├── css/
│   │   ├── style.css          # Core design system, typography & layouts
│   │   └── landing.css        # Landing hero and video modal styles
│   └── js/
│       └── main.js            # Frontend JavaScript logic
└── templates/
    ├── base.html              # Base Jinja2 layout (Navbar & Footer)
    ├── landing.html           # Landing page with video modal
    ├── login.html             # User login page
    ├── register.html          # User registration page
    ├── terms.html             # Terms & Conditions
    └── privacy.html           # Privacy Policy
```

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask 3.x, Jinja2
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3 (Flexbox & CSS Grid), Vanilla JavaScript (ES6+)
- **Testing**: `pytest`, `pytest-flask`

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/37AKSHAYJAYANT/claude.git
cd claude/expense-tracker
```

### 2. Set up a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

Open your browser and navigate to:
**[http://127.0.0.1:5001](http://127.0.0.1:5001)**

---

## 🌐 Routes Overview

| Method | Route | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Landing page with hero banner & video demo modal |
| `GET` | `/login` | User login page |
| `GET` | `/register` | User registration page |
| `GET` | `/terms` | Terms and Conditions |
| `GET` | `/privacy` | Privacy Policy |
| `GET` | `/logout` | User logout endpoint *(Step 3)* |
| `GET` | `/profile` | User profile page *(Step 4)* |
| `GET` | `/expenses/add` | Add new expense *(Step 7)* |
| `GET` | `/expenses/<id>/edit` | Edit existing expense *(Step 8)* |
| `GET` | `/expenses/<id>/delete`| Delete an expense *(Step 9)* |

---

## 🧪 Testing

Run the test suite using `pytest`:

```bash
pytest
```

---

## 📄 License

This project is licensed under the MIT License.

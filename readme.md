# Premium Flask Todo App

A beautiful, modern, and responsive To-Do list application built with Python and Flask. It features a premium dark-mode aesthetic with glassmorphism UI elements, and supports smooth drag-and-drop reordering for both lists and tasks.

## Features

- **Multiple Lists:** Create and manage separate to-do lists.
- **Task Management:** Add, complete, and delete tasks within each list.
- **Drag-and-Drop Reordering:** Easily change the order of your lists and tasks with smooth micro-animations.
- **Premium UI:** Dark-mode design with glassmorphism cards, modern typography (Inter font), and subtle hover effects.
- **SQLite Database:** Lightweight and fast local database using SQLAlchemy.

## Technologies Used

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML5, Vanilla CSS, Vanilla JavaScript
- **Libraries:** SortableJS (for drag-and-drop)
- **Typography:** Google Fonts (Inter)

## Folder Structure

```text
todoapp/
├── app/
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── requirements.txt
├── run.py
└── todo.db
```

## Setup Instructions

Follow these steps to run the application locally:

### 1. Clone or Download the Repository
Make sure you are in the project's root folder (`todoapp`).

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install Flask and Flask-SQLAlchemy using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server. The database (`todo.db`) and tables will automatically be initialized if they don't exist yet.

```bash
python run.py
```

### 5. Open in Browser
Open your web browser and navigate to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)
```
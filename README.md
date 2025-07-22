# Personal Task Manager

A Django web application for managing personal tasks with user authentication, categories, due dates, and priority levels.

## Features

- User authentication (registration, login, logout)
- Task CRUD operations (Create, Read, Update, Delete)
- Task categories and tags
- Due date management
- Task priority levels
- Task completion tracking

## Requirements

- Python 3.8+
- Django 4.2+

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task_manager
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Contributing

This project follows issue-driven development with proper Git workflow including branching and pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
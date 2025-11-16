# Wiki - Encyclopedia Web Application

A Wikipedia-like online encyclopedia built with Django as part of Harvard's CS50 Web Programming with Python and JavaScript course.

## 📋 Project Overview

This web application allows users to view, create, edit, and search encyclopedia entries written in Markdown format. The project demonstrates fundamental concepts in web development including server-side rendering, form handling, and dynamic content generation.

## ✨ Features

- **Entry Pages**: View encyclopedia entries rendered from Markdown to HTML
- **Index Page**: Browse all available encyclopedia entries
- **Search Functionality**: Search for entries with autocomplete suggestions
- **Create New Entry**: Add new encyclopedia entries using Markdown syntax
- **Edit Entry**: Modify existing entries with a pre-populated form
- **Random Page**: Navigate to a random encyclopedia entry
- **Markdown to HTML Conversion**: Automatic rendering of Markdown content

## 🛠️ Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS
- **Content Format**: Markdown
- **Template Engine**: Django Templates

## 🚀 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/michaela2024/cs50-wiki.git
cd cs50-wiki
```

2. Install dependencies (if applicable):
```bash
pip install -r requirements.txt
```

3. Run the Django development server:
```bash
python manage.py runserver
```

4. Open your browser and navigate to `http://127.0.0.1:8000`

## 📁 Project Structure

```
wiki/
├── encyclopedia/        # Main Django app
│   ├── views.py        # View functions for handling requests
│   ├── urls.py         # URL routing
│   ├── templates/      # HTML templates
│   └── util.py         # Utility functions for entry management
├── entries/            # Markdown files for encyclopedia entries
├── wiki/               # Django project settings
└── manage.py           # Django management script
```

## 🎯 Key Learning Outcomes

This project helped me develop skills in:
- Django framework architecture (models, views, templates)
- HTTP request/response cycle
- Form handling and validation
- File I/O operations in Python
- Markdown parsing and HTML generation
- URL routing and dynamic path handling
- Template inheritance and context passing

## 🔍 Implementation Highlights

- **Search with Substring Matching**: Returns exact matches or suggests similar entries
- **Markdown Conversion**: Uses Python-Markdown library for content rendering
- **Error Handling**: Graceful handling of non-existent entries with custom 404 pages
- **Clean URLs**: RESTful URL patterns for intuitive navigation

## 📚 Course Information

This project is part of **CS50's Web Programming with Python and JavaScript** offered by Harvard University. The course covers web development using Django, JavaScript, and modern web technologies.

## 🤝 Acknowledgments

Project specifications and starter code provided by Harvard's CS50 course.

---

**Note**: This is an educational project created for learning purposes.

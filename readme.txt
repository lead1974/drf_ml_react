# Django DRF ML React Project Setup

## Virtual Environment Setup

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
- Windows:
```bash
.\venv\Scripts\activate 
OR deactivate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure
- Backend: Django + Django REST Framework
- Frontend: React
- ML: Python ML libraries

## Django Project Setup

1. Create Django project:
```bash
django-admin startproject backend .
```


2. Create main app:
```bash
python manage.py startapp core
```

3. Apply migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run development server:
```bash
python manage.py runserver
```



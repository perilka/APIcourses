# APIcourses
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-5.0%2B-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)](https://www.docker.com/)

Production-ready Django REST API with Docker + Nginx, Swagger docs, pagination and filtering.

## Features
- Full Docker + docker-compose deployment (`up --build`)
- Nginx reverse proxy (production-grade routing)
- Swagger `/swagger/` & ReDoc `/redoc/` via drf-yasg
- Pagination (25 items), search, django-filter
- Auto-migrate + superuser creation on first start
- Multi-stage Dockerfiles + entrypoint.sh
- Ready for CI/CD and cloud deployment (Railway, Render, AWS, etc.)

## Stack
- Django 5 · DRF · drf-yasg · django-filter
- Nginx · Docker · PostgreSQL-ready

## Installation & Run

1. Clone the repository:
```bash
git clone https://github.com/perilka/APIcourses.git
cd APIcourses
```
2. Build and run with Docker:
```bash
docker-compose up --build
```
3. Access Swagger: `/swagger/`.
4. Admin panel: `/admin/` (create superuser via container).

For local dev:
```bash
cd APIproject
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver
```

## Project Structure

```text
APIcourses/
├── APIproject/         # Django project + management app
├── nginx/              # Production nginx config
├── docker-compose.yml
├── entrypoint.sh
└── requirements.txt
```

---

*Developed by 🐳 perilka 🐳 to demonstrate production-ready Django REST deployment with Docker & Nginx. Explore my resume and another repositories for similar production work!!!*

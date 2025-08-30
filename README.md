# University Courses API

API для управления университетами, курсами и связью между ними. Реализовано на Django и Django REST Framework.

---

## Модели

- **University** — `name`, `country`  
- **Course** — `title`, `description`  
- **UniversityCourse** — `university`, `course`, `semester`, `duration_weeks` (курс не может повторяться в одном семестре для одного университета)

---

## Эндпоинты

### Университеты
- CRUD: `/universities/`  
- `/universities/{id}/courses/` — все курсы университета  
- `/universities/{id}/course-stats/` — количество курсов и средняя длительность  

### Курсы
- CRUD: `/courses/`  
- Поиск и фильтрация по `title`  

### UniversityCourse
- CRUD: `/university-courses/`  
- Поиск по `course__title` и `university__name`  
- Фильтрация по `course__title` и `semester`  
- Сортировка по `duration_weeks`  

---

## Установка

```bash
git clone <repo>
cd <project>
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Админ-панель

- `/admin/` — Django админ-панель

## Swagger / OpenAPI

- `/swagger/` — документация API через drf-yasg

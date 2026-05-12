# Notes — заметки (Vue + Django REST)

Монорепозиторий: SPA на **Vue 3 / Vite / Tailwind**, API на **Django 6 + Django REST Framework**, данные в **PostgreSQL**.

## Структура

| Каталог    | Назначение                          |
| ---------- | ----------------------------------- |
| `backend/` | Django-проект, REST API `api/v1/`   |
| `frontend/`| Vue-приложение (Vite dev-сервер)    |

## Требования

- **Python** 3.12+ (совместимо с Django 6)
- **Node.js** `^20.19` или `>=22.12`
- **Docker** (опционально) — только для PostgreSQL

## База данных

PostgreSQL можно поднять из каталога `backend/`:

```bash
cd backend
docker compose up -d
```

Переменные `DB_USER`, `DB_PASSWORD`, `DB_NAME` должны совпадать с настройками в `.env` бэкенда (см. ниже).

## Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Создайте файл `backend/.env` (значения подставьте свои):

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Миграции и сервер:

```bash
python manage.py migrate
python manage.py runserver
```

API по умолчанию: **http://127.0.0.1:8000/**  
Админка Django: **http://127.0.0.1:8000/admin/**  

Основные маршруты API:

- `GET/POST` — `http://127.0.0.1:8000/api/v1/notes/`
- `GET/PUT/PATCH/DELETE` — `http://127.0.0.1:8000/api/v1/notes/<id>/`

## Frontend

```bash
cd frontend
npm install
npm run dev
```

Приложение: **http://localhost:5173/** (порт Vite по умолчанию).

Клиент ожидает API по адресу `http://localhost:8000/api/v1` (см. `frontend/src/services/api.js`). Бэкенд должен быть запущен на порту **8000**.

### Сборка и превью продакшена

```bash
npm run build
npm run preview
```

## Линтинг (frontend)

```bash
cd frontend
npm run lint
npm run format
```

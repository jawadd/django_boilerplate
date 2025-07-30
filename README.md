# 🛠️ Django Boilerplate with JSON Config, Custom User Model & Exception Logging

This is a clean Django boilerplate project featuring:

- 🔐 `config.json` for settings (no `.env`)
- 🧑‍💼 Custom user model (`AbstractUser`)
- 🧾 Structured `ExceptionError` logging model
- ⚙️ Dynamic DB config (SQLite default, PostgreSQL ready)
- 📦 `requirements.txt` included
- 🎯 Ready for static/media file deployment
- 🔒 Secure `.gitignore` for open source

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/jawadd/django_boilerplate.git
cd django-boilerplate
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create and configure `config.json`

Create `config.json` in the root:

```json
{
  "SECRET_KEY": "your-secret-key",
  "DEBUG": true,
  "ALLOWED_HOSTS": ["127.0.0.1", "localhost"],
  "DATABASE_URL": "sqlite:///db.sqlite3",
  "_POSTGRES_TEMPLATE": "postgres://user:password@localhost:5432/dbname"
}
```

### 5. Run migrations and start the server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 📦 Features

### ✅ `config.json` instead of `.env`
- Easy to manage and override settings via JSON

### ✅ Custom User Model
- Based on Django's `AbstractUser`
- Future-proofed for profile field extensions

### ✅ Exception Logging
- `ExceptionError` model logs:
  - Error type, message, traceback, path, timestamp
- Viewable in Django Admin

### ✅ Static and Media Files
- Ready for deployment with `STATIC_ROOT` and `MEDIA_ROOT`
- Served automatically during development

---

## 🧾 Admin Access

Create a superuser to access Django admin:

```bash
python manage.py createsuperuser
```

Then visit: http://127.0.0.1:8000/admin/

---

## 🤝 Contributing

Pull requests are welcome. Please follow Django conventions and keep commits atomic and clean.

---

## 📄 License

MIT License. Use freely and modify for your own projects.

---

## ✨ Credits

Created by [Jawad Hussain](https://github.com/jawadd) to provide a professional and extensible starting point for Django projects.

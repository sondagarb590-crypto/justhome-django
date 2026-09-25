# 🏠 JustHome - Real Estate Website (Django Backend)

## Features
- ✅ User Registration & Login
- ✅ Add / Edit / Delete Properties
- ✅ Property Search & Filter (by city, price, type)
- ✅ Contact Form (messages saved in database)
- ✅ Newsletter Subscribe
- ✅ Admin Panel (manage everything)
- ✅ Property Images Upload
- ✅ Featured Properties

---

## Setup Instructions

### Step 1 - Python install karo
Download from: https://www.python.org/downloads/
(Python 3.10 or higher)

### Step 2 - Open Project Folder
```
cd justhome_project
```

### Step 3 - Create Virtual Environment (recommended)
```
python -m venv venv
```
Activate karo:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### Step 4 - Requirements install
```
pip install -r requirements.txt
```

### Step 5 - Database setup 
```
python manage.py makemigrations
python manage.py migrate
```

### Step 6 - Admin user 
```
python manage.py createsuperuser
```
Ya directly:
```
python manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); U.objects.create_superuser('admin','admin@test.com','admin123')"
```

### Step 7 - Server run
```
python manage.py runserver
```

---

## URLs
| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| All Listings | http://127.0.0.1:8000/properties/ |
| Add Property | http://127.0.0.1:8000/properties/add/ |
| Register | http://127.0.0.1:8000/register/ |
| Login | http://127.0.0.1:8000/login/ |
| Contact | http://127.0.0.1:8000/contact/ |
| My Profile | http://127.0.0.1:8000/profile/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## Folder Structure
```
justhome_project/
│
├── manage.py
├── requirements.txt
├── setup_and_run.bat     (Windows shortcut)
├── setup_and_run.sh      (Mac/Linux shortcut)
│
├── justhome_project/     (project settings)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── justhome/             (main app)
    ├── models.py         (Database models)
    ├── views.py          (Page logic)
    ├── urls.py           (URL routing)
    ├── forms.py          (Forms)
    ├── admin.py          (Admin panel)
    ├── templates/        (HTML pages)
    └── static/           (CSS/JS/Images)
```

---

## One-Command Setup (Windows)
Double-click `setup_and_run.bat`

## One-Command Setup (Mac/Linux)
```
chmod +x setup_and_run.sh && ./setup_and_run.sh
```

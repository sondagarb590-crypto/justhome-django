@echo off
echo ========================================
echo   JustHome Django Setup Script
echo ========================================

echo.
echo [1/5] Installing requirements...
pip install -r requirements.txt

echo.
echo [2/5] Running database migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo [3/5] Creating superuser (admin)...
echo from django.contrib.auth import get_user_model; U = get_user_model(); U.objects.filter(username='admin').exists() or U.objects.create_superuser('admin', 'admin@justhome.com', 'admin123') | python manage.py shell

echo.
echo [4/5] Collecting static files...
python manage.py collectstatic --noinput 2>nul

echo.
echo [5/5] Starting server...
echo.
echo ========================================
echo   Server running at: http://127.0.0.1:8000
echo   Admin panel:        http://127.0.0.1:8000/admin
echo   Admin login:        admin / admin123
echo ========================================
echo.
python manage.py runserver
pause

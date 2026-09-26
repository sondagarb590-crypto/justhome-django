#!/bin/bash
echo "========================================"
echo "  JustHome Django Setup Script"
echo "========================================"

echo ""
echo "[1/4] Installing requirements..."
pip install -r requirements.txt

echo ""
echo "[2/4] Running database migrations..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "[3/4] Creating admin user..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
U = get_user_model()
if not U.objects.filter(username='admin').exists():
    U.objects.create_superuser('admin', 'admin@justhome.com', 'admin123')
    print('Admin created: admin / admin123')
else:
    print('Admin already exists')
"

echo ""
echo "[4/4] Starting server..."
echo ""
echo "========================================"
echo "  Server: http://127.0.0.1:8000"
echo "  Admin:  http://127.0.0.1:8000/admin"
echo "  Login:  admin / admin123"
echo "========================================"
echo ""
python manage.py runserver

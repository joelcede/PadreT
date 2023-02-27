activateEnviroment=venv/Scripts/activate
source enviroment.sh

if [ -d "venv" ];then
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "Activate..."
    else
        echo 'activating virtual environment'
        source $activateEnviroment
    fi
else
    echo 'creating virtual environment'
    python -m venv venv

    echo 'activating virtual environment'
    source $activateEnviroment
fi

if pip freeze | grep "djangorestframework" > /dev/null; then
  echo "El módulo está instalado"
else
  echo "El módulo no está instalado"
  cd backend
  pip install -r requirements.txt
fi

if [ -n "$VIRTUAL_ENV" ]; then 
    cd backend
    echo 'makemigrations database....'
    python manage.py makemigrations

    echo 'migrate database....'
    python manage.py migrate

    echo 'RUN APLICATION......'
    python manage.py runserver
else 
    echo "Entorno virtual no activado"; 
fi
# cd backend
# python manage.py createsuperuser --username=arced --email=admin@example.com --noinput
# echo "123456789" | python manage.py changepassword admin


# python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True).first())"

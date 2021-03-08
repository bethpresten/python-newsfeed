
web: gunicorn "app.create_app()" --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
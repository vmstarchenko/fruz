web: gunicorn --pythonpath src "core.wsgi:application"
worker: ./src/manage.py runscript clock --pythonpath=src
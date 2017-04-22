# truz

['509', '509', '420', '313', '322', '327', '432', '310', '219', '317', '301', '622', '311', '501', '402', '308', '306', '511', '304', '412', '605', '505', '205', '503', '435', '618', '416', '300', '400', '513']
gunicorn --pythonpath src "core.wsgi:application"
worker: ./src/manage.py runscript clock --pythonpath=src

## TODO:
  - add update by cron (Нужна привязка к карточке, заменю на костыль)
  - favicon.ico (DONE, но нужно переделать)
  - domain name (Нужна привязка к карточке)

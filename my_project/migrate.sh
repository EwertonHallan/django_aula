cd /Users/ewerton.hallabn/Desktop/Django/my_project/

python manage.py makemigrations

python manage.py migrate

#comandos do banco:
   # lista os comandos sql contidos no arquivo migrate
   # python manage.py sqlmigrate app_name migrate_file_name
   # gera comando para limpar a base de dados (delete's)
   # python manage.oy selflush
   # faz uma carga no bando de dados com base no arquivo json
   # python manage.py loaddata file_name_json --app app_name -i
   # faz uma exportacao dos dados para arquivo json
   # python manage.py dumpdata [app_name[.model_name] ...] --output file_name.json 


#fonte: https://docs.djangoproject.com/pt-br/1.11/ref/django-admin/#django-admin-sqlmigrate


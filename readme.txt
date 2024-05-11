Nota: 
 - Si quieres crear un nuevo proyecto debes escribir: django-admin startproject myproject
 - Si añadiste más librerías al entorno virtual del proyecto, debes ingresar el siguiente comando en cmd: pip freeze > requirements.txt
 - Si se quiere hacer de nuevo las migraciones de las clases a la base de datos, se utiliza: python manage.py makemigrations
   Luego se utiliza: python manage.py migrate


Para instalar los paquetes necesarios debes: 

1 - Verificar si python está instalado correctamente con: python --version
2 - Crear un entorno virtual usando: python -m venv venv
3 - Dar permisos varios: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
4 - Activar el entorno virtual usando: .\venv\Scripts\activate
5 - Verificar que el prompt de tu terminal tenga al inicio: (venv)
6 - Escribir: pip install -r requirements.txt
# Practica 13 Django

## Descripció

Aquest projecte Django gestiona les dades d'alumnes i professors del curs DAW2A. Inclou models, vistes i rutes per accedir a la informació, i està connectat a una base de dades PostgreSQL.

### Requisits previs

Python 3.11+

Django

PostgreSQL

## Instal·lació i configuració

### Clonar el repositori:

git clone https://github.com/rdalmau23/Django_Centre.git
cd tic_bcn_inicials_alumnat

### Crear i activar l'entorn virtual:

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows

### Instal·lar dependències:

pip install -r requirements.txt

## Configurar PostgreSQL:

CREATE DATABASE tic_bcn_inicials_alumnat;
CREATE USER rdalmau WITH PASSWORD 'rdc041';
ALTER ROLE rdalmau SET client_encoding TO 'utf8';
ALTER ROLE rdalmau SET default_transaction_isolation TO 'read committed';
ALTER ROLE rdalmau SET timezone TO 'Europe/Madrid';
GRANT ALL PRIVILEGES ON DATABASE tic_bcn_inicials_alumnat TO rdalmau;

### Modificar settings.py per connectar a la base de dades:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tic_bcn_inicials_alumnat',
        'USER': 'rdalmau',
        'PASSWORD': 'rdc041',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## Aplicar migracions:

python manage.py makemigrations
python manage.py migrate

Crear un superusuari per a l'administració:

python manage.py createsuperuser

(Introdueix el teu usuari i contrasenya)

## Execució

- Iniciar el servidor de desenvolupament:

- python manage.py runserver

- Accedir a l'aplicació:

- Web: http://127.0.0.1:8000/centre

- Admin: http://127.0.0.1:8000/admin

## Rutes Principals

/alumnes/ - Llista d'alumnes

/alumnes/<id>/ - Detall d'un alumne

/professors/ - Llista de professors

/professors/<id>/ - Detall d'un professor

## Vistes de l'Aplicació

### Llista d'Estudiants  
Aquesta vista mostra tots els estudiants registrats al sistema amb la seva informació bàsica.  
![Llista d'Estudiants](img/students.png)

### Detall d'un Estudiant  
Vista detallada d'un estudiant concret amb tota la seva informació acadèmica.  
![Detall d'un Estudiant](img/student_detail.png)

### Llista de Professors  
Es mostren tots els professors registrats al centre amb la seva informació rellevant.  
![Llista de Professors](img/teachers.png)

### Detall d'un Professor  
Vista amb tota la informació detallada d'un professor en concret.  
![Detall d'un Professor](img/teacher_detail.png)

### Panell d'Administració  
Accés al panell d'administració de Django per gestionar estudiants, professors i altres dades.  
![Panell d'Administració](img/admin.png)


## Autor

### Rafel Dalmau

## Llicència

### Aquest projecte està sota la llicència MIT.


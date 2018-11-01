Legal Accord and Unravel
========================

A Django application for indexing, analysing, and comparing EULA, ToS, and other documents.


    pip install --upgrade Django psycopg2-binary typing docutils celery django-celery-beat django-celery-results spacy
    pip install --upgrade django-extensions django-debug-toolbar mypy typed-ast deepdiff
    

Database setup
--------------

Requires PostgreSQL, with a server version >= 9.4.

    $ sudo apt update && sudo apt install postgresql postgresql-contrib

To use postgresql for development:

    $ sudo -u postgres createuser --createdb --pwprompt unravel_db
    $ sudo -u postgres createdb --owner=unravel_dev unravel_db
    $ sudo -u postgres psql
    # GRANT ALL PRIVILEGES ON DATABASE unravel_db TO unravel_dev;
    # CREATE EXTENSION IF NOT EXISTS pg_trgm;
    
To drop the database:

    $ sudo -u postgres dropdb unravel_db
    
To get a postgres command line:

    $ sudo -u postgres psql

Website Setup
-------------

Create a superuser: 

     $ ./manage.py createsuperuser


Pages / Views
-----

- Document - Latest (or other versions) with results: 
    - GET - list - /documents
    - POST - create - /documents
    - PUT/PATCH - update (new version) - /documents/:ID:
    - GET - show latest version - /documents/:ID:
    - GET - show content only - /documents/:ID:/content
    - GET - show diff with prev version - /documents/:ID:/diff
    - GET - show diff with prev version - /documents/:ID:/diff/:VERSION:
    - GET - show particular version - /documents/:ID:/versions/:VERSION:
    - GET - show content for version - /documents/:ID:/versions/:VERSION:/content
    - GET - show diff with prev version for version - /documents/:ID:/versions/:VERSION:/diff
    - GET - show diff with specified version for version - /documents/:ID:/versions/:VERSION:/diff/:VERSION:
    
- Tag - a single tag, with links to documents that have that tag
    - GET - list - /tags/
    - POST - create - /tags/
    - PUT/PATCH - update - /tags/:SLUG:
    - PUT/PATCH - update - /tags/:ID:
    - GET - show tag and documents - /tags/:SLUG:
    - GET - show tag and documents - /tags/:ID:
    
- Result - with links to documents used to create the result
    - GET - list - /annotations
    - GET - show with documents - /annotations/:ID:


Notes
-----

Use LogEntry to record changes: 

- https://stackoverflow.com/questions/7905106/adding-a-log-entry-for-an-action-by-a-user-in-a-django-app#7905253
- https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#logentry-objects


Create first migration without models?


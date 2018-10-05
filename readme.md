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

Notes
-----

Use LogEntry to record changes: 

- https://stackoverflow.com/questions/7905106/adding-a-log-entry-for-an-action-by-a-user-in-a-django-app#7905253
- https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#logentry-objects


Create first migration without models?


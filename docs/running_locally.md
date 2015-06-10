# Running Locally

This guide assumes you are running on a Mac with [Homebrew](http://brew.sh/) installed.

You will need the following running on your local computer:

 * [Postgres](http://postgresapp.com/)
 * Redis (`brew install redis`)
 * Python 3 (`brew install python3`)
 * [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)

Once those are installed, create yourself a virtual python env:
    
    $ mkdir ~/Projects/editus
    $ cd ~/Projects/editus
    $ mkvirtualenv --python=/usr/local/bin/python3 editus 
    $ workon editus
    $ pip install -r requirements-dev.txt

Now edit your new environment's postactivate hook:

    $ vim $WORKON_HOME/editus/bin/postactivate

Append the following content (ensuring the values are correct):

    export PYTHONPATH=/path/to/editus/src
    export DJANGO_SETTINGS_MODULE=editus.settings.local
    export REDIS_URL=redis://127.0.0.1:6379/0
    export DATABASE_URL=postgres://127.0.0.1:5432/editus
    # Ensure foreman displays output
    export PYTHONUNBUFFERED=true

Now activate the new settings by running the following (again):

    $ workon editus

Now setup your database:

    $ django-admin.py migrate

Tell foreman to use `Procfile.local` rather than `Procfile`:

    $ echo "procfile: Procfile.local" > .foreman

Now run foreman to start the development server, celery, and the docs server:

    $ foreman start

And you should be good to go! You can now access:

 * The app: [http://127.0.0.1:8000](http://127.0.0.1:8000) 
 * The docs: [http://127.0.0.1:8001](http://127.0.0.1:8001) 




# Running Locally

This guide assumes you are running on a Mac with [Homebrew](http://brew.sh/) installed.

You will need the following running on your local computer:

 * [Postgres](http://postgresapp.com/)
 * Redis (`brew install redis`)
 * Python 3 (`brew install python3`)
 * [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)

Once those are installed, create yourself a virtual python env:
    
    $ mkdir ~/Projects/djskel
    $ cd ~/Projects/djskel
    $ mkvirtualenv --python=/usr/local/bin/python3 djskel 
    $ workon djskel
    $ pip install -r requirements-dev.txt

Now edit your new environment's postactivate hook:

    $ vim $WORKON_HOME/djskel/bin/postactivate

Append the following content (ensuring the values are correct):

    export PYTHONPATH=/path/to/djskel/src
    export DJANGO_SETTINGS_MODULE=djskel.settings.local
    export REDIS_URL=redis://127.0.0.1:6379/0
    export DATABASE_URL=postgres://postgres@127.0.0.1:5432/djskel
    export SECRET_KEY="random-string-here"
    # Ensure foreman displays output
    export PYTHONUNBUFFERED=true
    alias run="foreman start"

Now activate the new settings by running the following (again):

    $ workon djskel

Now setup your database:

    $ django-admin.py migrate

Tell foreman to use `Procfile.local` rather than `Procfile`:

    $ echo "procfile: Procfile.local" > .foreman

Now run foreman to start the development server, celery, and the docs server:

    $ foreman start
    # OR, using the alias setup in postactivate, simply:
    $ run

And you should be good to go! You can now access:

 * The app: [http://127.0.0.1:8000](http://127.0.0.1:8000) 
 * The docs: [http://127.0.0.1:8001](http://127.0.0.1:8001) 

## Testing Skeleton App

The skeleton app can be tested by running:

    python src/djskel/utils/tests_skeleton.py

You will need to be running foreman in another terminal window.
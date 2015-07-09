# Running Locally

This guide assumes you are running on a Mac with [Homebrew](http://brew.sh/) installed.

You will need the following running on your local computer:

 * [Postgres](http://postgresapp.com/)
 * Redis (`brew install redis`)
 * Python 3 (`brew install python3`)
 * [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)

First, let's set your project name:
    
    :::shell
    $ PRJNAME=exampleprj # Change this!

Once those are installed, create yourself a virtual python env:
    
    :::shell
    $ mkdir ~/Projects/$PRJNAME
    $ cd ~/Projects/$PRJNAME
    $ mkvirtualenv --python=/usr/local/bin/python3 $PRJNAME 
    $ workon $PRJNAME
    $ pip install -r requirements-dev.txt

Now edit your new environment's postactivate hook:

    :::shell
    $ vim $WORKON_HOME/$PRJNAME/bin/postactivate

Append the following content (ensuring the values are correct):

    :::shell
    export PYTHONPATH=/path/to/exampleprj/src
    export DJANGO_SETTINGS_MODULE=exampleprj.settings.local
    export REDIS_URL=redis://127.0.0.1:6379/0
    export DATABASE_URL=postgres://postgres@127.0.0.1:5432/exampleprj
    export SECRET_KEY="random-string-here"
    export AWS_ACCESS_KEY_ID="[aws-access-key-here]"
    export AWS_SECRET_ACCESS_KEY="[aws-secret-here]"
    export AWS_STORAGE_BUCKET_NAME="name-of-static-and-media-files-bucket"
    
    # Ensure foreman displays output
    export PYTHONUNBUFFERED=true
    alias run="foreman start"

Now activate the new settings by running the following (again):

    :::shell
    $ workon $PRJNAME

Now setup your database:

    :::shell
    $ django-admin.py migrate

Tell foreman to use `Procfile.local` rather than `Procfile`:

    :::shell
    $ echo "procfile: Procfile.local" > .foreman

Now run foreman to start the development server, celery, and the docs server:

    :::shell
    $ foreman start
    # OR, using the alias setup in postactivate, simply:
    $ run

And you should be good to go! You can now access:

 * The app: [http://127.0.0.1:8000](http://127.0.0.1:8000) 
 * The docs: [http://127.0.0.1:8001](http://127.0.0.1:8001) 

## Test Skeleton App

The app should now be setup. You can test this by running (you'll need to be running 
foreman in another terminal window):

    python src/$PRJNAME/utils/tests_skeleton.py

This will:

1. Queue a dummy celery task
2. Load the registration page
3. Send a test email to ``DEFAULT_FROM_EMAIL``
4. Load the docs homepage

!!! warning
    Note that this is **not** done in a test environment.

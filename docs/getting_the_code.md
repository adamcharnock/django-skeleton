# Getting the Code

To get setup with this project do the following:
    
    # Get the code
    $ PRJNAME=exampleprj
    $ cd ~/Projects
    $ git clone git@github.com:priestc/django-skeleton.git $PRJNAME
    $ cd $PRJNAME
    
    # Change the origin remote to your new repo
    $ git remote rename origin skeleton
    $ git remote add origin git@github.com:you/your-repo.git
    
    # Replace references to djskel with your project name
    $ env LC_CTYPE=C LANG=C find ./ -type f ! -path '*/\.*' -exec sed -i "" -e "s/djskel/$PRJNAME/g" {} \;
    
    
# Skeleton Project Setup

To get setup with the skeleton project do the following:
    
    :::shell
    # Get the code
    $ PRJNAME=exampleprj
    $ cd ~/Projects
    $ git clone git@github.com:priestc/django-skeleton.git $PRJNAME
    $ cd $PRJNAME
    
    # Change the origin remote to your new repo
    $ git remote rename origin skeleton
    $ git branch --unset-upstream master
    $ git remote add --fetch origin git@github.com:you/your-repo.git
    $ git push -u origin master
    
    # Replace references to djskel with your project name
    $ env LC_CTYPE=C LANG=C find ./ -type f ! -path '*/\.*' -exec sed -i "" -e "s/djskel/$PRJNAME/g" {} \;
    $ mv src/djskel src/$PRJNAME
    
    # Now commit your changes
    # git add .
    # git commit -a -m "Customising skeleton for new project"

Next: [Get it running locally](running_locally.md)

!!! note "Not using PyCharm?"
    If you are not using PyCharm then removing the ``.idea`` directory would 
    be a good idea.

## PyCharm Setup (optional)

    $ cd .idea
    $ env LC_CTYPE=C LANG=C find ./ -type f ! -exec sed -i "" -e "s/djskel/$PRJNAME/g" {} \;
    $ mv djskel.iml $PRJNAME.iml 

Using PyCharm go to:

1. *File -> Open*, and select your project directory.
2. Once open, set your python interpreter in *Preferences -> Project -> Project Interpreter*.    

You should find the 
project loads with the various directories (src, templates, assets) configured correctly, 
and extraneous directories ignored.

!!! note
    The above PyCharm config assumes you keep your projects in ~/Projects. 
    If this is not the case you will need to edit the files within 
    ``.idea/`` accordingly. 


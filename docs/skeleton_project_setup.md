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
    $ git remote add origin git@github.com:you/your-repo.git
    $ git branch --set-upstream master origin/master
    
    # Replace references to djskel with your project name
    $ env LC_CTYPE=C LANG=C find ./ -type f ! -path '*/\.*' -exec sed -i "" -e "s/djskel/$PRJNAME/g" {} \;

Next: [Get it running locally](running_locally.md)

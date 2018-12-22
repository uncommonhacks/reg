while :
do
    git fetch --all;
    git reset --hard origin/deploy;
    pipenv run python3 manage.py collectstatic --no-input; 
    pipenv run python3 manage.py makemigrations; 
    pipenv run python3 manage.py migrate; 
    pipenv run zappa update;
    sleep 30;
done

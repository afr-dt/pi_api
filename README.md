# Simple Api

## Requirements

- Python 3.8
- PostgreSQL 9.6 or higher
- Clone this repo
- Create two database for dev and test
- Change name .env_template to .env and change secretes
- Create a virtualenv with `venv` or `pipenv`
- Run `pip install -r requirements.txt`
- Create tables `python manage.py db upgrade`
- Run to dev `python manage.py run`
- Run test `python manage.py test`

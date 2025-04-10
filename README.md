# About chatbot

<< What does this project do >>

## Problem statement

- << ______ >>
- is a problem for << ------ >>
- because << --------- >>.


## Getting the local server running


- Install `mysql`: https://dev.mysql.com/doc/refman/8.4/en/installing.html


```bash
# Clone repository
git clone <repo-link>
cd chatbot

# creating virtual env
uv venv --python=python3.13
source .venv/bin/activate

# create a new database

mysql -u root -p --default-character-set=utf8mb4
CREATE DATABASE chatbot_db CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE DATABASE test_chatbot_db CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

# Create MySQL users
create user 'py-user' identified by 'p@@sWord';
grant all privileges on chatbot_db.* to 'py-user';
grant all privileges on test_chatbot_db.* to 'py-user';
flush privileges;
exit


# install dependencies
uv pip install -r requirements/requirements-dev.txt

# install pre-commit hooks
pre-commit install

# Provide database authentications
cp .env.sample .env
# update the .env file with mysql username, password and database name
vi .env

# Create database and tables
python manage.py migrate

# Start development server
python manage.py runserver
```


## Deployment

```bash
git push live
```

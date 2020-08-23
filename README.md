# Flask-Grakn

Simple proof of concept repo to test integration of grakn into a flask website.

Quickstart

### Setup your environment ###
1. git clone repo
2. cd flask-grakn
3. pipenv install
4. pipenv shell

### Setup Grakn keyspace from examples folder ###
1. Start the Grakn Sever
2. Via terminal while inside the Grakn distribution, run: ./grakn console -k phone_calls -f path-to-the-cloned-repo/schemas/phone-calls-schema.gql
3. cd examples
4. Via terminal while inside the virtual pipenv shell, run: python migrate_csv.py

### Run the Flask app ###
5. export FLASK_APP=graknapp
6. export FLASK_ENV=development
7. flask run
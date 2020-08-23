
from grakn.client import GraknClient

from flask import Flask

from config import BaseConfig



def create_app():
    # Create Flask server app
    server = Flask(__name__)
    server.config.from_object(BaseConfig)
    connect_grakn(server)
    register_blueprints(server)

    return server


def connect_grakn(server):
    with GraknClient(uri="localhost:48555") as client:
        with client.session(keyspace="phone_calls") as session:
            ## session is open
            with session.transaction().read() as read_transaction:
                answer_iterator = read_transaction.query("match $x isa person; get; limit 10;").get()
                persons = [ans.get("x") for ans in answer_iterator]
                for person in persons:
                    print("Retrieved person with id " + person.id)
        ## session is closed
    ## client is closed


def register_blueprints(server):
    from app.views.home_views import index_bp

    server.register_blueprint(index_bp)

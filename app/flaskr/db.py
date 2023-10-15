import sqlite3
import click
from flask import current_app, g

def init_app(app):
    # tells Flask to call that function when cleaning up after returning the response
    app.teardown_appcontext(close_db)
    # add a new command that can be called with the flask command
    # flask --app flaskr init-db
    app.cli.add_command(init_db_command)

# @click command: defines a command line command called init-db that calls the init_db function
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

def get_db():
    # g is a special object that is unique for each request
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row tells the connection to return rows that behave like dicts
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

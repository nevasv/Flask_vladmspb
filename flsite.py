import sqlite3
import os
from flask import Flask, render_template, request

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = '65fc74dc8f453b48af092bb103344f88aca00260'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()

    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()


# Python console>>  from flsite import create_db
# create_db()

if __name__ == "__main__":
    app.run(debug=True)

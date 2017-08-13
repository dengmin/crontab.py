from flask import Flask

from flask_peewee.db import Database


app = Flask(__name__)
app.config.from_object('config.DEV')

db = Database(app)

if __name__ == '__main__':
    app.run(port=8080)
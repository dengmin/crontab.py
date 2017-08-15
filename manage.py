
from flask import Flask
from flask_peewee.db import Database
from app.scheduler import Scheduler
app = Flask(__name__)
app.config.from_object('config.Dev')

db = Database(app)

app.scheduler = Scheduler()
app.scheduler.start()

from app.views import *

if __name__ == '__main__':
    app.run(port=8080)
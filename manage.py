
from core import create_app
from config import Dev
from flask_peewee.db import Database

app = create_app(Dev)
db = Database(app)

if __name__ == '__main__':
    app.run(port=8080)
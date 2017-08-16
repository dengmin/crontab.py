
from app import create_app
from config import Dev
app = create_app(Dev)

if __name__ == '__main__':
    app.run(port=8080)
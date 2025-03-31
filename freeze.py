from your_flask_app import app  # Import your Flask app
from flask_frozen import Freezer

freezer = Freezer(app)

@freezer.register
def index():
    return app.send_static_file('index.html')  # Adjust as necessary

if __name__ == '__main__':
    freezer.freeze()

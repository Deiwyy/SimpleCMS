from flask import Flask
from flask_session import Session
from config import config
from db.connection import close_db
from blueprints.main import main_bp

app = Flask(__name__)
app.config.from_mapping(config)

Session(app)  # Setup Flask-Session

app.register_blueprint(main_bp)

@app.teardown_request
def teardown_request(exception):
    close_db(exception)

if __name__ == "__main__":
    app.run(debug=True)

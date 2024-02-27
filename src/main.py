from flask import Flask
from app import views

app = Flask(__name__)

if __name__ == "__main__":
    views.init(app)

    app.config["SECRET_KEY"] = "3038cd18-e471-46a7-bf8e-a197c5359608"
    app.run(debug=True, port=8001)

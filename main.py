from flask import  Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return "<h1> hello from yossef </h1>"



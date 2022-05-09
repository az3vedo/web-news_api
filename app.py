from flask import Flask

app = Flask(__name__)

@app.route('/status')
def health_check():
    return "app is running"
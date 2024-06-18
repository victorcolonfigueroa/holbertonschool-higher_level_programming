from flask import Flask, request, jsonify

app = Flask(__name__)


"""create a route for the api"""
@app.route('/')
def home():
    return "Home page"


""" run the flask server"""

if __name__ == '__main__':
    app.run(debug=True)
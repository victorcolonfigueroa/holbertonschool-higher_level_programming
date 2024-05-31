from flask import Flask, jsonify, request

app = Flask(__name__)

user = {}

@app.route('/')
def home():
    return "Welcome to the API Flask!"

user ={
    "jane":{"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john":{"name": "John", "age":30, "city": "New York"} 
}

@app.rout('/data')
def data():
    return jsonify(list(user.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route("/user/<username>")
def get_user(username):
    user = user.get(username)
    if user:
        return jsonify(user)
    else:
        return "User Not found", 404
    
@app.route("/add_user", methods=["POST"])
def add_user():
nesc_data = request.get_json()
username = nesc_data.get("username")

if username and username is not users:
    users[username]={
        "name": nesc_data["name"],
        "age": nesc_data["age"],
        "city": nesc_data["city"]
    }
    return jsonify(user{username}),201
else:
    return "User already exists or invalid data", 400

if __name__ == "__main__":
    app.run()

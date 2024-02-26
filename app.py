from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    user_agent = request.headers.get('User-Agent')
    data = {
        "message": "Welcome 2024!",
        "user_agent": user_agent
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug=True, port=4001)

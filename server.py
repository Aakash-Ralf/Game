from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the score
score_data = {"score": 0}

@app.route('/update_score', methods=['POST'])
def update_score():
    global score_data
    data = request.get_json()
    score_data["score"] = data.get("score", 0)
    return jsonify(score_data)

@app.route('/get_score', methods=['GET'])
def get_score():
    return jsonify(score_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


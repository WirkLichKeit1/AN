from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from AN import traduzir_to_AN, traduzir_from_AN

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/translateToAN', methods=['POST'])
def traduzirtoAN():
    data = request.get_json()
    text = data.get('text', '')
    result = traduzir_to_AN(text)
    return jsonify({'result': result})

@app.route('/api/translateFromAN', methods=['POST'])
def traduzirfromAN():
    data = request.get_json()
    AN = data.get('AN', '')
    result = traduzir_from_AN(AN)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
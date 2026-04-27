from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

# ✅ Add this route
@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/rank', methods=['POST'])
def calculate_rank():
    data = request.json
    matrix = np.array(data['matrix'])
    rank = np.linalg.matrix_rank(matrix)
    return jsonify({"rank": int(rank)})

if __name__ == '__main__':
    app.run(debug=True)

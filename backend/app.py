from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app, resources={r"/bfhl": {"origins": "http://localhost:3000"}})

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        try:
            data = request.json.get('data', [])
            print('Received data:', data)  # Log received data

            numbers = [item for item in data if isinstance(item, str) and item.isdigit()]
            alphabets = [item for item in data if isinstance(item, str) and item.isalpha()]
            highest_lowercase = max((char for char in alphabets if char.islower()), default='')

            response = {
                "is_success": True,
                "user_id": "Sandip Datta",  # Replace with your actual user_id
                "email": "dattasandip2003@gmail.com",  # Replace with your actual email
                "roll_number": "21BCE1163",  # Replace with your actual roll number
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
            }

            print('Sending response:', response)  # Log response
            return jsonify(response), 200
        except Exception as e:
            print('Error:', str(e))  # Log any errors
            return jsonify({"error": str(e)}), 400

    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
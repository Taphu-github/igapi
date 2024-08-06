from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    
    data = request.get_json()
    print(json.dumps(data, indent=4))  # For debugging


    return f'<p>{data}</p>'

if __name__ == '__main__':
    app.run(debug=True)

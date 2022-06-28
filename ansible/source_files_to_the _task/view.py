from flask import Flask, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_root():
    return json.dumps('Deployed!')


@app.route('/health', methods=['GET'])
def get_health():
    return json.dumps({'Healthy': True})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

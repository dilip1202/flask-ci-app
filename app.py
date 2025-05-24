from flask import Flask

# This is Flask App and now testing it
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Dilip!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

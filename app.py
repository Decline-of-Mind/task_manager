import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world... again"

if __name__ == '__main__':
    app.run(host=environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
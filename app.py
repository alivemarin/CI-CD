from flask import Flask
app = Flask (__name__)

@app.route ('/')
def hello_world ():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# This is a simple Flask application that runs on port 5000.
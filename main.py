from flask import Flask
app = Flask(__name__)

@app.root("/")
def hello():
    return 'Welcome to Python!!!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
    

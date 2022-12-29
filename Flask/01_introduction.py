from flask import Flask

app = Flask(__name__) # Act as wsgi application

@app.route('/') # Decorator 
def welcome():
    return 'Hello World'

@app.route('/members') # Decorator 
def members():
    return 'Hello World members'


if __name__ == '__main__':
    app.run(debug=True)

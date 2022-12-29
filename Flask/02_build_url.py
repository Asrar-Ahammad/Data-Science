# Build URL dynamicaly

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello world'

@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and marks score '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed entered score : '+str(score)
    
# result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks<50:
        result = 'fail'
    else:
        result = 'success'
    # return 'The result of person is ' + result
    return redirect(url_for(result,score = marks))

if __name__ == '__main__':
    app.run(debug = True)
# Working with Jinja2 template engine
'''
{%....%} for statements,conditions, for loops
{{    }} expressions to print output
{#....#} for comments
'''
# Intrgrating HTML with Flask
# HTTP verb GET and POST

from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def marks():
    return render_template('index.html')

@app.route('/submit', methods = ['POST','GET'])
def submit():
    total_score = 0
    science = float(request.form['science'])
    maths = float(request.form['maths'])
    datascience = float(request.form['datascience'])
    cprog = float(request.form['cprog'])
    total_score = (science+maths+datascience+cprog)/4
    return render_template('results_04.html',result = total_score)


if __name__ == '__main__':
    app.run(debug=True)
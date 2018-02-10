from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "counter_secret"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def counter():
    count = session['count']
    if request.form['hidden'] == 'add_two':
        session['count'] += 1
    session['hidden'] = 'add_two'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('count')    
    return redirect('/')
app.run(debug=True)


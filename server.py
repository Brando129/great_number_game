from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)

app.secret_key = "bananas are better than apples"

@app.route('/')
def index():
    if "number" not in session:
        session['number'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)
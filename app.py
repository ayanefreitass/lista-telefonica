from flask import Flask, render_template, session


app = Flask(__name__)
app.secret_key = '123'

user = {}

@app.route('/')
def index():
    return render_template('login.html', e=False)
 
@app.route('/logar')
def logar():
    session['origem'] = 'logar'
    return render_template('logar.html')
    

if __name__ == '__main__':
    app.run(debug=True)

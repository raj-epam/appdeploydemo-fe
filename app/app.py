# app.py
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/fe')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

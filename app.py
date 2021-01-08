from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_form():
    title = "Rules for Courtships"
    return render_template('form.html', title=title)

@app.route('/data')
def data():
    return 'test'
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/development')
def development():
    return render_template('development.html')

if __name__ == '__main__':
    app.run()

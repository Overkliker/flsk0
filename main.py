from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<templates>')
def index(templates):
    return render_template('index.html', Title=templates)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

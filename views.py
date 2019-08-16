from flask import render_template

from ytdl import app


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

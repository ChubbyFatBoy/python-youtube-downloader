import os
from pytube import YouTube
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_KEY')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST', 'GET'])
def download():
    if request.method == 'POST':
        url = str(request.form["url"])
        yt = YouTube(url)
        print(yt.title)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download('/home/lildogzsixpack')
        print("Has been successfully downloaded")
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

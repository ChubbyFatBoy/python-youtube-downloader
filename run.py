from __future__ import unicode_literals
import os
import youtube_dl
from flask import Flask, render_template, request
import config

app = Flask(__name__)
app.secret_key = config.flask_key


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST', 'GET'])
def download():
    if request.method == 'POST':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
			'outtmpl': os.path.join(config.download_folder, "%(title)s-%(id)s.%(ext)s"),
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([request.form["url"]])
    else:
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
	os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), config.download_folder), exist_ok=True)
	app.run(host=config.host, port=config.port, debug=config.debug)
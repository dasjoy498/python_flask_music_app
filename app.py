from flask import Flask, render_template, current_app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/music_album')
def play_music():
    return render_template('./audio.html')


@app.route('/audio.css')
def load_audio_css():
    return current_app.send_static_file('./audio.css')


@app.route('/index_css.css')
def load_index_css():
    return current_app.send_static_file('./index_css.css')


@app.route('/favicon.ico')
def load_favicon():
    return current_app.send_static_file('./images/favicon.ico')


@app.route('/images/dnld1.ico')
def load_download_icon():
    return current_app.send_static_file('./images/dnld1.ico')


@app.route('/songs/Humnava.mp3')
def load_song_Humnava():
    return current_app.send_static_file('./songs/Humnava.mp3')


@app.route('/songs/HamariAdhuriKahani.mp3')
def load_song_HamariAdhuriKahani():
    return current_app.send_static_file('./songs/HamariAdhuriKahani.mp3')


@app.route('/songs/YehKaisiJagah.mp3')
def load_song_YehKaisiJagah():
    return current_app.send_static_file('./songs/YehKaisiJagah.mp3')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, url_for, request

from youtube_transcript_api import YouTubeTranscriptApi

def get_transc():
    text = YouTubeTranscriptApi.get_transcript(video_id)
    transc = []
    for x in range(len(text)):
        transc.append(text[x]['text'])


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        video_id=request.form['video_id']
        try:
            text = YouTubeTranscriptApi.get_transcript(video_id)
            transc=[]
            for x in range(len(text)):
                transc.append(text[x]['text'])
            file=transc
            return render_template('index.html',file=file)
        except:
            file = ['There was an error']
            return render_template('index.html', file=file)
    else:
        return render_template('index.html')

@app.route('/hello')
def hello(): 
    return "hey"

if __name__ == "__main__":
    app.run(debug=True)
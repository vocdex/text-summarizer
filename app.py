from flask import Flask, request, render_template
from model import TextSummarizer

app = Flask(__name__)

summarizer = None

def load_model():
    global summarizer
    summarizer = TextSummarizer()


@app.route("/")
def render_index():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def generate_summary():

    if not summarizer:
        load_model()

    text = request.form['input_box']
    output = summarizer(text)
    return render_template('index.html', input=text, output=output)

if __name__ == "__main__":
    app.run()

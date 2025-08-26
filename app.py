from flask import Flask, render_template_string, request
from googletrans import Translator
app = Flask(__name__)
TEMPLATE = "<h2>Translator</h2><form method='post'><textarea name='text'>{{text}}</textarea><br><input name='src' value='auto'> to <input name='dest' value='en'><button>Translate</button></form>{% if translated %}<p>{{translated}}</p>{% endif %}"
@app.route('/', methods=['GET','POST'])
def index():
    translated=''; text=''
    if request.method=='POST':
        text=request.form.get('text',''); src=request.form.get('src','auto'); dest=request.form.get('dest','en')
        try: translated=Translator().translate(text, src=src, dest=dest).text
        except Exception as e: translated=str(e)
    return render_template_string(TEMPLATE, translated=translated, text=text)
if __name__=='__main__': app.run(debug=True)

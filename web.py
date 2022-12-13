from flaskext.markdown import Markdown
from unittest import result
from flask import Flask, render_template, url_for, request
import spacy
from spacy import displacy, load

nlp = spacy.load("./model-best")
colors = {"ORGANISASI": "#FF6666", "NAMA_ORANG": "#FCFF7D", "HARI": "#58E0A7", "TANGGAL": "#9BA3EB",
          "HARGA": "#FFCACA", "PRODUK_PERTANIAN": "#FFE9C5", "PENYAKIT": "#FB8D62", "LOKASI": "#9E7676", "MUSIM": "#CFD2CF"}
options = {"colors": colors}

# init App
app = Flask(__name__)
Markdown(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form')
def form():
    return render_template('form.html')


# @app.route('/result')
# def resultt():
#    return render_template('result.html')


@app.route('/result', methods=["GET", "POST"])
def resultt():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        docx = nlp(rawtext)
        html = displacy.render(docx, style='ent', options=options)
        result = html

    return render_template('result.html', rawtext=rawtext, result=result)


if __name__ == '__main__':
    app.run(debug=True)

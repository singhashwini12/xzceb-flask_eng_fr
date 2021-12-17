import machinetranslation as mt
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", template_folder="templates")

@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    return mt.translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    return mt.translator.french_to_english(text_to_translate)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)
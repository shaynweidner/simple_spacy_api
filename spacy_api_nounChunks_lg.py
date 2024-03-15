from flask import Flask, request, jsonify
from flask_cors import CORS
import en_core_web_lg

app = Flask(__name__)
CORS(app)
nlp = en_core_web_lg.load()


@app.route('/extract_phrases', methods=['POST'])
def extract_phrases():
    data = request.json
    text = data['text']
    doc = nlp(text)
    phrases = list(dict.fromkeys(chunk.text for chunk in doc.noun_chunks))
    phrases.sort(key=lambda phrase: (-sum(1 for other in phrases if phrase.lower() in other.lower() and phrase.lower() != other.lower()), -len(phrase), phrase.lower()))
    return jsonify(phrases=phrases)


if __name__ == '__main__':
    app.run(port=23692, host="0.0.0.0")

from flask import Flask, request, jsonify
from flask_cors import CORS
import en_core_web_sm
import sys
import os
from sense2vec import Sense2VecComponent

app = Flask(__name__)
CORS(app)
nlp = en_core_web_sm.load()
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
s2v_path = os.path.join(base_path, "s2v_reddit_2019_lg")
s2v = nlp.add_pipe("sense2vec")
s2v.from_disk(s2v_path)

print(base_path)
print(s2v_path)
print(os.listdir(s2v_path))




@app.route('/extract_phrases', methods=['POST'])
def extract_phrases():
    data = request.json
    text = data['text']
    doc = nlp(text)
    phrases = doc._.s2v_phrases
    phrases = [str(phrase) for phrase in phrases]
    phrases.sort(key=lambda phrase: (-sum(1 for other in phrases if phrase.lower() in other.lower() and phrase.lower() != other.lower()), -len(phrase), phrase.lower()))
    return jsonify(phrases=phrases)


if __name__ == '__main__':
    app.run(port=23692, host="0.0.0.0")

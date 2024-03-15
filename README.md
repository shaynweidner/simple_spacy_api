This repo is primarily a demo of how to make a simple flask API that utilizes spaCy, and furthermore how to bundle it up with pyInstaller.

A version with a small spaCy model included is in the releases.  This will only work for the x86-64 architecture, running windows (AFAIK).

Otherwise, to run the endpoint locally:

```
git clone https://github.com/shaynweidner/simple_spacy_api
cd simple_spacy_api
python -m venv venv
# activate the new virtual environment, e.g. source ./venv/bin/activate
pip install -r requirements.txt
python spacy_api_nounChunks_sm.py
```

depending on what specifically you are expecting to run, you can certainly slim down the requirements.txt file

If you would like to bundle this into an executable, you'll also need to :

```
pip install pyinstaller
pyinstaller --onefile --add-data '.\venv\Lib\site-packages\en_core_web_sm:en_core_web_sm' --add-data 's2v_reddit_2019_lg:s2v_reddit_2019_lg' --clean --recursive-copy-metadata sense2vec .\spacy_api_sense2vecPhrases_sm_lg.py
```

Again, depending on what you want to package up, you can slim this down or adjust the pyinstaller directives.
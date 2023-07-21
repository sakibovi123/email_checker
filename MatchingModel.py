import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def detect_symbols(email):
    # load data
    filename = 'file.csv'
    df = pd.read_csv(filename)
    
    print(df)

    tokens = word_tokenize(email)
    
    tokens = [w.lower() for w in tokens]
    
    import string
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    words = [word for word in stripped if word.isalpha()]
    
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    print(words[:100])


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('punkt')
tokens = word_tokenize("support@affimedia.com")
nltk.download('stopwords')

words = ["over", "@"]
stop_words = set(words)

tokens = [w for w in tokens if not w in stop_words]
print(tokens)
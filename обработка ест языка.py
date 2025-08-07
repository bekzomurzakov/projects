import pandas as pd

data = {
    'review': [
        "Это отличный продукт! Очень рекомендую.",
        "Ужасное качествоб зря потратил деньги.",
        "Просто нормальный товар, ничего особенного.",
        "Очень доволен покупкой! Отличное качество.",
        "Продукт пришел сломанным, ужасный сервис."
    ],
    'label': ['positive', 'negative', 'neutral', 'positive', 'negative']
}

df = pd.DataFrame(data)
print(df)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Load stop-words
nltk.download('stopwords')
nltk.download('punkt')

# Function
def preprocess_text(text):
    text = text.lower()

    text = text.translate(str.maketrans("", "", string.punctuation))

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("russian"))
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)

df['cleaned_review'] = df['review'].apply(preprocess_text)
print(df[['review', 'cleaned_review']])

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['cleaned_review'])
y = df['label']

print('Матрица признаков: ')
print(X.toarray())

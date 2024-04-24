import nltk
from collections import Counter
nltk.download("stopwords")
from nltk.corpus import stopwords
nltk.download('punkt')
stop_words = stopwords.words('english')
file_path = "paragraphs.txt"
with open(file_path, 'r') as f:
    text = f.read()
from nltk.tokenize import word_tokenize,sent_tokenize 
text = text.lower()
words = nltk.word_tokenize(text)

stop_words = set(stopwords.words('english'))
word_counts = Counter(word for word in words if word not in stop_words)
print("Word Frequency Counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
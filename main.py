import matplotlib
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def get_frequency(item):
    return item[1]

# Czyszczenie tekstu
url = "https://lv.wikipedia.org/wiki/Latvija"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()
text = re.sub(r'\W+', ' ', text.lower())
words = text.split()

# Prawo Zipfa
word_counts = Counter(words)
ranked_words = sorted(word_counts.items(), key=get_frequency, reverse=True)

df = pd.DataFrame(ranked_words, columns=["Word", "Frequency"])
df["Rank"] = df["Frequency"].rank(ascending=False, method="first")
print(df)

plt.plot(df["Rank"], df["Frequency"])
plt.xlabel("Rank(r)")
plt.ylabel("Frequency(f)")
plt.title("Prawo Zipfa w łotewskich tekstach")

plt.show()
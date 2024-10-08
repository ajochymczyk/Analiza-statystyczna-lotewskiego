from bs4 import BeautifulSoup
from collections import Counter
import re
import matplotlib
import requests
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt_tab')
matplotlib.use('TkAgg')

def get_item(item):
    return item[1]

# Czyszczenie tekstu
'''''
url = "https://lv.wikipedia.org/wiki/Latvija"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()
'''''
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

sentences = sent_tokenize(text)

clean_sentences = []
for sentence in sentences:
    clean_sentence = re.sub(r'[^a-zāčēģīķļņōšūžA-ZĀČĒĢĪĶĻŅŌŠŪŽ ]+', ' ', sentence.lower())  # Usuń wszystko poza literami i spacjami
    clean_sentences.append(clean_sentence)

# Prawo Zipfa
words = ' '.join(clean_sentences).split()
word_counts = Counter(words)
ranked_words = sorted(word_counts.items(), key=get_item, reverse=True)

df = pd.DataFrame(ranked_words, columns=["Word", "Frequency"])
df["Rank"] = df["Frequency"].rank(ascending=False, method="first")
df["R*F"] = df["Rank"] * df["Frequency"]

print(df)
df.to_csv("zipf_table.csv", index=False)
plt.plot(df["Rank"], df["Frequency"])
plt.xlabel("Rank(r)")
plt.ylabel("Frequency(f)")
plt.title("Prawo Zipfa w łotewskich tekstach")

plt.show()

# Graf
graph = nx.Graph()
'''
for i in range(len(words) - 1):
    graph.add_edge(words[i], words[i+1])
'''
for clean_sentence in clean_sentences:
    sentence_words = clean_sentence.split()
    # krawędzie między sąsiadującymi słowami, które są w jednym zdaniu
    sentence_words = [word for word in sentence_words if len(word) > 1]
    for i in range(len(sentence_words) - 1):
        graph.add_edge(sentence_words[i], sentence_words[i + 1])

plt.figure(figsize=(20, 20))

pos = nx.circular_layout(graph)
#pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_size=100, font_size=7, node_color="lightblue", edge_color="gray")
plt.title("Graf słów języka łotewskiego")
plt.savefig("graph.png")
plt.show()

degrees = dict(graph.degree())
sorted_degrees = sorted(degrees.items(), key=get_item, reverse=True)

core = 100
core_vertices = sorted_degrees[:core]

print("Najczęściej występujące 100 słów- rdzeń języka:")
for vertex, degree in core_vertices:
    print(f"Słowo (wierzchołek) {vertex}, liczba sąsiadów: {degree}.")

# Rdzeń grafu
core_graph = graph.subgraph(v[0] for v in core_vertices)
plt.figure(figsize=(20, 20))
pos = nx.circular_layout(core_graph)
nx.draw(core_graph, pos, with_labels=True,  node_size=300, font_size=10, node_color='lightblue', edge_color='gray')
plt.title("Rdzeń języka łotewskiego")
plt.savefig("core_graph.png")
plt.show()

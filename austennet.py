import re, itertools
import networkx as nx
import matplotlib.pyplot as plt

# let's load the text in from file
with open('pride.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text = text[text.find("Chapter 61")+len("Chapter 61"):text.find("End of the Project Gutenberg EBook")].strip()
text = re.sub(r'\n {6}', ' ', text)
text = text.replace(".", "")

# How do we divide this text:
chapters = re.split(r"Chapter \d{1,2}", text)

# divide into paragraphs
paragraphs = text.split("\n")

with open('characters.txt', 'r', encoding='utf8') as rf:
    characters = rf.read().split("\n")
    characters = [character.split(", ") for character in characters]

# save edge information
character_assoc_dictionary = dict()

for chapter in paragraphs:
    appears = []
    for character in characters:
        for name in character:
            if name in chapter:
                appears.append(character[0])
                break
    relationships = itertools.combinations(sorted(appears),2)
    for relationship in relationships:
        if relationship in character_assoc_dictionary:
            character_assoc_dictionary[relationship] += 1
        else:
            character_assoc_dictionary[relationship] = 1

G = nx.Graph()

for character in characters:
    G.add_node(character[0])

for edge, weight in character_assoc_dictionary.items():
    G.add_edge(edge[0], edge[1], weight=weight)

print(G.edges().data())

nx.draw(G,with_labels=True)
plt.show()
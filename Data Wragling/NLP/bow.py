import re
from collections import Counter

# Sample corpus
documents = [
    "I love NLP",
    "I love deep learning",
    "NLP is fun"
]

# Preprocess the documents
def preprocess(doc):
    # Convert to lowercase
    doc = doc.lower()
    # Remove punctuation
    doc = re.sub(r'[^\w\s]', '', doc)
    tokens = re.findall(r'\b\w+\b', doc)
    return tokens

tokenized_docs = [preprocess(doc) for doc in documents]

# Create a vocabulary
vocab = sorted(set(word for doc in tokenized_docs for word in doc))
word_to_index = {word: i for i, word in enumerate(vocab)}

# Create the BoW representation
def create_bow(doc):
    bow = [0] * len(vocab)
    for word in doc:
        if word in word_to_index:
            bow[word_to_index[word]] += 1
    return bow
bow_docs = [create_bow(doc) for doc in tokenized_docs]

# Display the results
for i, doc in enumerate(bow_docs):
    print(f"Document {i+1}: {documents[i]}")
    print("BoW representation:", doc)
    print()
# Display the vocabulary
print("Vocabulary:", vocab)
print("Word to Index Mapping:", word_to_index)
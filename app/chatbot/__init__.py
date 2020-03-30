import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import nltk
import json
import random



EXCLUDED_CHARACTERS = ('?')
INTENTS_FILENAME = "intents.json"
MODEL_FILENAME = "model.h5"


stemmer = nltk.LancasterStemmer()


# Returns all the the data for responses from the intents file.
# Must be the same the bot was trained on.
def load_intents_data(t_filename):
    data = {}
    with open(t_filename) as file:
        data = json.load(file)

    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:

            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    words = [stemmer.stem(w.lower())
             for w in words if w not in EXCLUDED_CHARACTERS]
    words = sorted(list(set(words)))
    labels = sorted(labels)

    return (data, words, labels, docs_x, docs_y)


# Create a one-hot enconded word bag
def word_bag(t_str, t_words):
    bag = [0 for _ in range(len(t_words))]

    s_words = nltk.word_tokenize(t_str)
    s_words = [stemmer.stem(w.lower()) for w in s_words]

    for s in s_words:
        for i, w in enumerate(t_words):
            if w == s:
                bag[i] = 1

    bag = np.array(bag)
    bag = bag.reshape(1, max(bag.shape))
    return bag

# Talk with the bot
def chat(t_model, t_data, t_words, t_labels, t_quit_cmd="quit"):
    print("Talk with me!")

    while True:
        inp = input("YOU: ")

        if inp.lower() == t_quit_cmd:
            break

        result = np.argmax(t_model.predict(word_bag(inp, t_words)))
        tag = t_labels[result]

        response = str()
        for intent in t_data["intents"]:
            if tag == intent["tag"]:
                response = random.choice(intent["responses"])

        print(response)


if __name__ == "__main__":

    data, words, labels, _, _ = load_intents_data(INTENTS_FILENAME)
    model = load_model(MODEL_FILENAME)

    chat(t_data=data, t_model=model, t_words=words, t_labels=labels)

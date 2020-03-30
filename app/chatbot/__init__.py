import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import nltk
import json
import random


nltk.download("punkt")

EXCLUDED_CHARACTERS = ('?')
INTENTS_FILENAME = "intents.json"
MODEL_FILENAME = "model.h5"


stemmer = nltk.LancasterStemmer()


# Returns all the the data for responses from the intents file.
# Must be the same the bot was trained on.
def load_intents_data(filename):
    data = {}
    with open(filename) as file:
        data = json.load(file)

    words = []
    labels = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:

            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    words = [stemmer.stem(w.lower())
             for w in words if w not in EXCLUDED_CHARACTERS]
    words = sorted(list(set(words)))
    labels = sorted(labels)

    return (data, words, labels)


# Create a one-hot enconded word bag
def word_bag(user_input, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(user_input)
    s_words = [stemmer.stem(w.lower()) for w in s_words]

    for s in s_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1

    bag = np.array(bag)
    bag = bag.reshape(1, max(bag.shape))
    return bag


DATA, WORDS, LABELS = load_intents_data(INTENTS_FILENAME)
MODEL = load_model(MODEL_FILENAME)


def respond(user_input):
    result = np.argmax(MODEL.predict(word_bag(user_input, WORDS)))
    tag = LABELS[result]
    response = str()
    for intent in DATA["intents"]:
        if tag == intent["tag"]:
            response = random.choice(intent["responses"])
    return response

if __name__ == "__main__":
    pass
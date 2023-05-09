from flask import Flask
import requests
import random
import json

app = Flask(__name__)

def shuffle_flashcards(flashcards):
    """
    Shuffles flashcards.
    """
    card_list = list(flashcards.keys())
    shuffled_flashcards = {}
    
    random.shuffle(card_list)

    for card in card_list:
        shuffled_flashcards[card] = flashcards[card]

    return shuffled_flashcards

url = 'http://127.0.0.1:56889/flashcards' # replace with your own url

flashcards = requests.get(url) # gets flashcards from url
flashcards = flashcards.json() # decodes json

@app.route('/shuffled-flashcards')
def shuffled_flashcards():
    """
    Posts shuffled flashcards at http://127.0.0.1:56899/shuffled-flashcards
    """
    result = shuffle_flashcards(flashcards)

    return json.dumps(result)

if __name__ == '__main__':
    app.run(port=56899, debug=True)

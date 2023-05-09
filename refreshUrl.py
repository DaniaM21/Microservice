import webbrowser
import time

url = 'http://127.0.0.1:56899/shuffled-flashcards'

# refreshes url so that flashcards are shuffled every 2 seconds
while True:
    webbrowser.open(url, new=0)
    time.sleep(2)

# Microservice
Flask Microservice that shuffles flashcards.

## Communication Contract
The following topics explain how to install the Microservice, how to request data, and how to receive data. A UML sequence diagram also shows how requesting and receiving data works.

### How to Install
On a terminal, run the command:
```bash
git clone https://github.com/DaniaM21/Microservice.git
```

This will make a local copy of Microservice.

Next, run the command:

```bash
make install
```

This will run Makefile and install all the required packages from requirements.txt.

### How to Request Data
To request data, post your flashcards in JSON format to a URL.

For example, if you were using Python, an example call would look like this:

```python
import requests

request_url = 'http://127.0.0.1:56889/flashcards' # replace with your own URL

flashcards = {'Spider-man': 'Peter Parker', 'Iron Man': 'Tony Stark', 'Captain America': 'Steve Rogers', 'Black Widow': 'Natasha Romanoff', 'Hulk': 'Bruce Banner'}

response = requests.post(request_url, json=flashcards)
```

The content of the URL should look like this:

<img width="329" alt="Flashcards in JSON format" src="https://user-images.githubusercontent.com/109312705/236991832-1763066c-64b7-438a-8c33-d8c9f0c88cb8.png">


### How to Receive Data
In the app.py file, change the URL to the URL where your flashcards are posted.

You can also change the port number from 56899 at the bottom of the file.

Then, run the following commands to run:

app.py
```bash
python3 app.py
```

refreshUrl.py
```bash
python3 refreshUrl.py
```

When app.py is run, the link http://127.0.0.1:56899/shuffled-flashcards is created.

It will post your flashcards in JSON format but in shuffled order.

Use an HTTP Request to read this content.

For example, using Python:

```python
import requests

url = 'http://127.0.0.1:56899/shuffled-flashcards'

flashcards = requests.get(url) # gets flashcards from url
flashcards = flashcards.json() # decodes json

# use shuffled flashcards in your program
```

The refreshUrl.py file will keep refreshing the link every two seconds for you so that when you go to receive flashcards again, the flashcards are shuffled continuously.

### UML Sequence Diagram

<img width="329" alt="UML Sequence Diagram" src="https://user-images.githubusercontent.com/109312705/236997621-cefa36ed-e4fa-4dd9-b336-a4766a5e5de6.png">

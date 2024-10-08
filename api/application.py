from flask import Flask, jsonify
from flask_cors import CORS
import random

application = Flask(__name__)

# Enable CORS for all origins
CORS(application)

# List of quotes
quotes = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."
]

@application.route('/api/quote', methods=['GET'])
def get_quote():
    # Select a random quote
    selected_quote = random.choice(quotes)
    return jsonify({'quote': selected_quote})

if __name__ == '__main__':
    application.run(debug=True)
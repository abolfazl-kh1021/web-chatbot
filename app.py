from flask import Flask, render_template, request, jsonify
import nltk
from nltk.stem import WordNetLemmatizer

# Initialize the Flask app
app = Flask(__name__)

# Initialize the Lemmatizer from NLTK

nltk.download("punkt")
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()

# Dictionary for basic responses
responses = {
    "hello": "Hello! How can I help you? 😊",
    "how are you": "I'm doing great! 😄",
    "name": "I'm a Python NLP chatbot 🤖",
    "bye": "Goodbye 👋",
}


@app.route("/")
def home():
    # Corrected: Flask automatically looks in the 'templates' folder.
    return render_template("index.html")


@app.route("/get", methods=["GET"])
def chatbot_response():
    user_input = request.args.get("msg")
    # Lemmatization: Convert words to their base form
    user_input = " ".join([lemmatizer.lemmatize(word) for word in user_input.split()])
    # Ensure the key is lowercase before lookup
    response = responses.get(user_input.lower(), "Sorry, I didn't understand that 😅")
    return jsonify(response=response)


if __name__ == "__main__":
    # This runs the app on http://127.0.0.1:5000/ by default
    app.run(debug=True)

from flask import Flask, render_template, request, g
import os
import ldclient
from ldclient import Context
from ldclient.config import Config
import uuid

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()

# List of egg facts
egg_facts = [
    "The largest chicken egg ever laid weighed 12 ounces!",
    "Eggs contain all 9 essential amino acids.",
    "The color of an egg's shell is determined by the breed of the chicken.",
    "Eggs can be stored in the refrigerator for up to 5 weeks.",
    "The average hen lays 300-325 eggs per year.",
    "Eggs are one of the few foods that naturally contain Vitamin D.",
    "The world record for most eggs laid by a chicken in one day is 7.",
    "Eggs are considered a complete protein source.",
    "The yolk color depends on the hen's diet.",
    "Eggs are one of the most versatile ingredients in cooking."
]

# List of egg jokes (question and answer)
egg_jokes = [
    {"question": "Why did the egg go to school?", "answer": "To get egg-ucated!"},
    {"question": "What do you call an egg from outer space?", "answer": "An egg-stra terrestrial!"},
    {"question": "Why did the Easter egg hide?", "answer": "Because it was a little chicken!"},
    {"question": "What do you call an egg that's afraid of everything?", "answer": "A chicken!"},
    {"question": "Why did the egg cross the road?", "answer": "To prove he wasn't a chicken!"},
    {"question": "What do you call an egg that's always late?", "answer": "An egg-stra slow egg!"},
    {"question": "Why was the Easter egg so good at stand-up comedy?", "answer": "Because it always cracked people up!"},
    {"question": "How do you send a letter to an Easter egg?", "answer": "By egg-spress delivery!"},
    {"question": "Why did the egg get promoted?", "answer": "Because it was egg-cellent at its job!"},
    {"question": "What do you call an egg that's a great dancer?", "answer": "An egg-straordinary mover!"}
]

@app.route("/")
def home():
    return render_template("index.html", facts=egg_facts)

if __name__ == '__main__':
    app.run(debug=True)


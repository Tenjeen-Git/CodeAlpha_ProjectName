import json
import string
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer (only runs first time)
nltk.download("punkt")

# Load FAQ data from JSON file
with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)

# Extract questions and answers separately
questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]


# Function to clean text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation (.,?! etc.)
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Break into words
    tokens = word_tokenize(text)

    # Join words back into sentence
    return " ".join(tokens)


# Clean all stored FAQ questions
processed_questions = [preprocess_text(q) for q in questions]

# Convert text into numeric vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)


# Function to find best answer
def get_best_answer(user_input):
    # Clean user input
    processed_input = preprocess_text(user_input)

    # Convert to vector
    input_vector = vectorizer.transform([processed_input])

    # Compare similarity with all questions
    similarity_scores = cosine_similarity(input_vector, question_vectors)

    # Get best match index
    best_match_index = similarity_scores.argmax()

    # Get best similarity score
    best_score = similarity_scores[0, best_match_index]

    # If score is too low, return default message
    if best_score < 0.4:
        return "Sorry, I could not find a good answer for that question."

    # Return matching answer
    return answers[best_match_index]
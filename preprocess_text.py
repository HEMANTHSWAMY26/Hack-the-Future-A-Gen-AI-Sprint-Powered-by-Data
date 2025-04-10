import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (run this only once)
import nltk
nltk.download('punkt')          # For tokenization
nltk.download('stopwords')      # For stopwords
nltk.download('wordnet')        # For lemmatization

def preprocess_text(text):
    """
    Preprocess text by performing the following steps:
    1. Convert to lowercase.
    2. Remove special characters, numbers, and punctuation.
    3. Tokenize the text.
    4. Remove stopwords.
    5. Lemmatize the tokens.
    """
    # Step 1: Convert to lowercase
    text = text.lower()
    
    # Step 2: Remove special characters, numbers, and punctuation
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    # Step 3: Tokenize the text
    tokens = word_tokenize(text)
    
    # Step 4: Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Step 5: Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join the tokens back into a single string
    preprocessed_text = " ".join(tokens)
    return preprocessed_text

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Sample text from Problem Statement 7: Customer Support Query
    sample_text = "I need help with my account login issue!"
    preprocessed_text = preprocess_text(sample_text)
    print("Original Text:", sample_text)
    print("Preprocessed Text:", preprocessed_text)
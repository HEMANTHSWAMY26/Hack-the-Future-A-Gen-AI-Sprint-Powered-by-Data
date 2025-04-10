import ollama

def summarize_query(query):
    """
    Generate a concise summary of the customer query using an Ollama-based model.
    """
    try:
        # Use gemma3:latest for summarization
        response = ollama.chat(
            model="gemma3:latest",  # Replace with the model you want to use
            messages=[{"role": "user", "content": f"Summarize the following query in one sentence: {query}"}]
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"Error generating summary: {e}")
        return None

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Sample queries to test the summarizer
    queries = [
        "I need help with my account login issue because I forgot my password.",
        "The software installation failed due to compatibility issues.",
        "I need assistance with resetting my account password.",
        "My payment gateway integration is failing, and I don't know why."
    ]

    for query in queries:
        summary = summarize_query(query)
        print("\nOriginal Query:", query)
        print("Summary:", summary)
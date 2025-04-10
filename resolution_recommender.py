import ollama

def recommend_resolution(query, historical_resolutions):
    """
    Recommend a resolution for the query based on historical data.
    """
    try:
        # Combine historical resolutions into a single string for context
        context = "\n".join(historical_resolutions)
        
        # Use gemma3:latest for resolution recommendation
        response = ollama.chat(
            model="gemma3:latest",  # Replace with the model you want to use
            messages=[{"role": "user", "content": f"Based on the following historical resolutions, recommend a solution for this query: Query: {query}\nHistorical Resolutions:\n{context}"}]
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"Error recommending resolution: {e}")
        return None

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Sample historical resolutions
    historical_resolutions = [
        "For forgotten passwords, reset the password using the 'Forgot Password' link.",
        "For software installation failures, ensure system compatibility and reinstall.",
        "For payment gateway issues, check API keys and network connectivity."
    ]

    # Sample queries to test the resolution recommender
    queries = [
        "I forgot my password and cannot log in.",
        "The software installation failed due to compatibility issues.",
        "My payment gateway integration is failing for unknown reasons."
    ]

    for query in queries:
        recommendation = recommend_resolution(query, historical_resolutions)
        print("\nQuery:", query)
        print("Recommended Resolution:", recommendation)
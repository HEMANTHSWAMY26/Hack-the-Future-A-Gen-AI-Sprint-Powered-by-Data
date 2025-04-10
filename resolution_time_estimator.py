import ollama

def estimate_resolution_time(query, historical_data):
    """
    Estimate the resolution time for the query based on historical data.
    """
    try:
        # Combine historical data into a single string for context
        context = "\n".join(historical_data)
        
        # Use gemma3:latest for resolution time estimation
        response = ollama.chat(
            model="gemma3:latest",  # Replace with the model you want to use
            messages=[{"role": "user", "content": f"Based on the following historical data, estimate the resolution time for this query: Query: {query}\nHistorical Data:\n{context}"}]
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"Error estimating resolution time: {e}")
        return None

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Sample historical data
    historical_data = [
        "Password reset issues typically take 1-2 hours to resolve.",
        "Software installation failures usually require 4-6 hours to fix.",
        "Payment gateway integration issues may take 1-2 business days to resolve."
    ]

    # Sample queries to test the resolution time estimator
    queries = [
        "I forgot my password and cannot log in.",
        "The software installation failed due to compatibility issues.",
        "My payment gateway integration is failing for unknown reasons."
    ]

    for query in queries:
        estimated_time = estimate_resolution_time(query, historical_data)
        print("\nQuery:", query)
        print("Estimated Resolution Time:", estimated_time)
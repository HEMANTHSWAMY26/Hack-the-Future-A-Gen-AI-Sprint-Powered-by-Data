import ollama

def extract_action(summary):
    """
    Extract actionable insights from the summarized query using an Ollama-based model.
    """
    try:
        # Use DistilBERT or a similar lightweight model for intent detection
        response = ollama.chat(
            model="gemma3:latest",  # Replace with the model you want to use
            messages=[{"role": "user", "content": f"Identify the key action required for the following summary: {summary}"}]
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"Error extracting action: {e}")
        return None

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Sample summaries to test the action extractor
    summaries = [
        "Customer needs help logging in due to a forgotten password.",
        "Software installation failed because of compatibility problems.",
        "Customer needs assistance resetting their account password.",
        "Payment gateway integration is failing for unknown reasons."
    ]

    for summary in summaries:
        action = extract_action(summary)
        print("\nSummary:", summary)
        print("Action:", action)
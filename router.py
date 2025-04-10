import ollama

def route_ticket(summary, priority):
    """
    Route the ticket to the appropriate team based on the summary and priority.
    """
    try:
        # Use gemma3:latest for routing decisions
        response = ollama.chat(
            model="gemma3:latest",  # Replace with the model you want to use
            messages=[{"role": "user", "content": f"Based on the following summary and priority, decide which team should handle this ticket: Summary: {summary}, Priority: {priority}"}]
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"Error routing ticket: {e}")
        return None

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Sample summaries and priorities to test the router
    tickets = [
        {"summary": "Customer needs help logging in due to a forgotten password.", "priority": "High"},
        {"summary": "Software installation failed because of compatibility problems.", "priority": "Medium"},
        {"summary": "Payment gateway integration is failing for unknown reasons.", "priority": "Critical"},
        {"summary": "Customer needs assistance resetting their account password.", "priority": "Low"}
    ]

    for ticket in tickets:
        summary = ticket["summary"]
        priority = ticket["priority"]
        assigned_team = route_ticket(summary, priority)
        print("\nSummary:", summary)
        print("Priority:", priority)
        print("Assigned Team:", assigned_team)
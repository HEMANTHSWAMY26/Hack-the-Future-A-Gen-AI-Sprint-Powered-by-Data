import ollama
import sqlite3

# Import agent functions
from summarizer import summarize_query
from action_extractor import extract_action
from router import route_ticket
from resolution_recommender import recommend_resolution
from resolution_time_estimator import estimate_resolution_time

# Database setup
def initialize_database():
    """
    Initialize the SQLite database to store ticket data.
    """
    conn = sqlite3.connect("customer_support.db")
    cursor = conn.cursor()

    # Create a table for tickets
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            issue_category TEXT,
            sentiment TEXT,
            priority TEXT,
            solution TEXT,
            resolution_status TEXT,
            date_of_resolution TEXT,
            conversation TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_to_database(ticket_data):
    """
    Save ticket data to the SQLite database.
    """
    conn = sqlite3.connect("customer_support.db")
    cursor = conn.cursor()

    # Insert ticket data into the table
    cursor.execute("""
        INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ticket_data["ticket_id"],
        ticket_data["issue_category"],
        ticket_data["sentiment"],
        ticket_data["priority"],
        ticket_data["solution"],
        ticket_data["resolution_status"],
        ticket_data["date_of_resolution"],
        ticket_data["conversation"]
    ))

    conn.commit()
    conn.close()

# Main workflow
def process_ticket(ticket_id, query, conversation, historical_resolutions, historical_data):
    """
    Process a customer ticket using the multi-agent framework.
    """
    print("\nProcessing Ticket ID:", ticket_id)

    # Step 1: Summarize the query
    summary = summarize_query(query)
    print("Summary:", summary)

    # Step 2: Extract actionable insights
    action = extract_action(summary)
    print("Action:", action)

    # Step 3: Route the ticket to the appropriate team
    priority = "High"  # Example priority (can be dynamically determined)
    assigned_team = route_ticket(summary, priority)
    print("Assigned Team:", assigned_team)

    # Step 4: Recommend a resolution
    recommendation = recommend_resolution(query, historical_resolutions)
    print("Recommended Resolution:", recommendation)

    # Step 5: Estimate resolution time
    estimated_time = estimate_resolution_time(query, historical_data)
    print("Estimated Resolution Time:", estimated_time)

    # Step 6: Save ticket data to the database
    ticket_data = {
        "ticket_id": ticket_id,
        "issue_category": "Login Issue",  # Example category (can be dynamically determined)
        "sentiment": "Frustrated",  # Example sentiment (can be dynamically determined)
        "priority": priority,
        "solution": recommendation,
        "resolution_status": "Pending",
        "date_of_resolution": "2023-11-01",  # Example date (can be dynamically determined)
        "conversation": conversation
    }
    save_to_database(ticket_data)
    print("Ticket data saved to the database.")

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Sample historical resolutions and data
    historical_resolutions = [
        "For forgotten passwords, reset the password using the 'Forgot Password' link.",
        "For software installation failures, ensure system compatibility and reinstall.",
        "For payment gateway issues, check API keys and network connectivity."
    ]

    historical_data = [
        "Password reset issues typically take 1-2 hours to resolve.",
        "Software installation failures usually require 4-6 hours to fix.",
        "Payment gateway integration issues may take 1-2 business days to resolve."
    ]

    # Sample tickets to test the integrated system
    tickets = [
        {
            "ticket_id": "TICKET_001",
            "query": "I forgot my password and cannot log in.",
            "conversation": "Customer: I forgot my password. Agent: No problem, let me help you reset it."
        },
        {
            "ticket_id": "TICKET_002",
            "query": "The software installation failed due to compatibility issues.",
            "conversation": "Customer: The software won't install. Agent: Can you confirm your system specifications?"
        }
    ]

    for ticket in tickets:
        process_ticket(
            ticket_id=ticket["ticket_id"],
            query=ticket["query"],
            conversation=ticket["conversation"],
            historical_resolutions=historical_resolutions,
            historical_data=historical_data
        )
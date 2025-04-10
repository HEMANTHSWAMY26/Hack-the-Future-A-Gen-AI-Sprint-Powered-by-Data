import pandas as pd
import os

def load_tickets(csv_path):
    """
    Load ticket data from a CSV file.
    """
    try:
        # Load the CSV file
        data = pd.read_csv(csv_path)
        
        # Strip spaces from column names
        data.columns = data.columns.str.strip()
        
        # Print the column names for debugging
        print("Columns in the CSV file:", data.columns)
        
        # Normalize text columns if they exist
        if 'Issue Category' in data.columns:
            data['Issue Category'] = data['Issue Category'].str.lower()
        else:
            print("Warning: 'Issue Category' column not found in the CSV file.")
        
        if 'Solution' in data.columns:
            data['Solution'] = data['Solution'].str.lower()
        else:
            print("Warning: 'Solution' column not found in the CSV file.")
        
        # Print the first few rows for debugging
        print("First few rows of the DataFrame:")
        print(data.head())
        
        return data
    except Exception as e:
        print(f"Error loading the CSV file: {e}")
        return None

def load_conversations(folder_path):
    """
    Load conversation logs from the conversations folder.
    """
    conversations = {}
    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            conversation_id = filename.split(".")[0]
            conversations[conversation_id] = content
    return conversations

# Example usage (for testing purposes)
if __name__ == "__main__":
    tickets = load_tickets("data_files/tickets.csv")  # Use forward slashes
    conversations = load_conversations("data_files\Conversation")  # Use forward slashes
    
    print(list(conversations.keys()))
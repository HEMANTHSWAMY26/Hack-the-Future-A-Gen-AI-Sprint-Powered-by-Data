# Hack-the-Future-A-Gen-AI-Sprint-Powered-by-Data


# AI-Driven Customer Support System

This project is a **multi-agent AI system** designed to streamline customer support operations by automating query summarization, action extraction, resolution recommendation, task routing, and resolution time estimation.

## Features
- **Query Summarizer**: Automatically generates concise summaries of customer queries.
- **Action Extractor**: Identifies actionable insights like escalations or follow-ups.
- **Routing Agent**: Assigns tickets to the appropriate team (e.g., technical support, customer service).
- **Resolution Recommender**: Recommends solutions based on historical data.
- **Resolution Time Estimator**: Predicts resolution times using historical trends.
- **Interactive UI**: Built with **Streamlit** for user-friendly interaction.

## Technologies Used
- **Ollama-based Models**: Lightweight AI models like TinyLlama-1.1B, Gemma-2B, and DistilBERT.
- **SQLite Database**: For storing ticket data and historical resolutions.
- **Python**: Primary programming language.
- **Streamlit**: For building an interactive web interface.

## Project Structure
```
AI_Customer_Support/
├── agents/                # Agent scripts (summarizer, router, etc.)
├── data/                  # Synthetic datasets and historical data
├── database/              # SQLite database setup
├── app/                   # Streamlit app files
├── main.py                # Main script integrating all agents
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Installation
1. Clone the repository
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app/app.py
   ```

## License
This project is licensed under the MIT License.


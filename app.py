import streamlit as st
from summarizer import summarize_query
from action_extractor import extract_action
from router import route_ticket
from resolution_recommender import recommend_resolution
from resolution_time_estimator import estimate_resolution_time

# Title and Description
st.title("AI-Driven Customer Support System")
st.markdown("""
This app demonstrates an AI-driven multi-agent system for efficient customer support.
The system summarizes queries, extracts actions, routes tickets, recommends resolutions, and estimates resolution times.
""")

# Input Form
st.header("Submit a Customer Query")
query = st.text_area("Enter the customer query here:", height=100)
priority = st.selectbox("Select the priority level:", ["Low", "Medium", "High", "Critical"])

if st.button("Process Query"):
    if not query.strip():
        st.error("Please enter a valid query.")
    else:
        # Step 1: Summarize the Query
        summary = summarize_query(query)
        st.subheader("Query Summary")
        st.write(summary)

        # Step 2: Extract Actionable Insights
        action = extract_action(summary)
        st.subheader("Action Required")
        st.write(action)

        # Step 3: Route the Ticket
        assigned_team = route_ticket(summary, priority)
        st.subheader("Assigned Team")
        st.write(assigned_team)

        # Step 4: Recommend Resolution
        historical_resolutions = [
            "For forgotten passwords, reset the password using the 'Forgot Password' link.",
            "For software installation failures, ensure system compatibility and reinstall.",
            "For payment gateway issues, check API keys and network connectivity."
        ]
        recommendation = recommend_resolution(query, historical_resolutions)
        st.subheader("Recommended Resolution")
        st.write(recommendation)

        # Step 5: Estimate Resolution Time
        historical_data = [
            "Password reset issues typically take 1-2 hours to resolve.",
            "Software installation failures usually require 4-6 hours to fix.",
            "Payment gateway integration issues may take 1-2 business days to resolve."
        ]
        estimated_time = estimate_resolution_time(query, historical_data)
        st.subheader("Estimated Resolution Time")
        st.write(estimated_time)

        # Final Output
        st.success("Query processed successfully!")
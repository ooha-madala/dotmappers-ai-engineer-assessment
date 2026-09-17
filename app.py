import streamlit as st
import sys
import os

# Allow importing from the app folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from app.query_engine import (
    get_summary,
    get_priority_count,
    get_category_average_rating,
    ask_gemini
)

st.set_page_config(
    page_title="Support Ticket AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Support Ticket AI Assistant")
st.write("Ask questions about the customer support ticket dataset.")

# Dashboard
st.subheader("📊 Ticket Overview")

summary = get_summary()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tickets", summary["total_tickets"])
col2.metric("Open Tickets", summary["open_tickets"])
col3.metric("Resolved Tickets", summary["resolved_tickets"])
col4.metric("Escalated Tickets", summary["escalated_tickets"])

st.divider()

# AI Question Answering
st.subheader("💬 Ask the AI")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: How many critical tickets are there?"
)

if st.button("Ask AI"):
    if question.strip():
        with st.spinner("Analyzing the support tickets..."):
            try:
                answer = ask_gemini(question)
                st.success("Answer")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
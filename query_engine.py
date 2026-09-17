import os
import pandas as pd
from google import genai
from data_loader import load_data


def get_summary():
    df = load_data()

    return {
        "total_tickets": len(df),
        "open_tickets": len(df[df["status"] == "Open"]),
        "resolved_tickets": len(df[df["status"] == "Resolved"]),
        "escalated_tickets": len(df[df["status"] == "Escalated"]),
    }


def get_priority_count(priority):
    df = load_data()

    result = df[df["priority"].str.lower() == priority.lower()]

    return len(result)


def get_category_average_rating(category):
    df = load_data()

    result = df[
        (df["category"].str.lower() == category.lower())
        & (df["customer_rating"].notna())
    ]

    if len(result) == 0:
        return None

    return round(result["customer_rating"].mean(), 2)


def ask_gemini(question):
    df = load_data()

    data_summary = df.to_string(index=False)

    client = genai.Client()

    prompt = f"""
You are an AI assistant for a customer support ticket dataset.

Answer the user's question using ONLY the dataset provided below.

Dataset:
{data_summary}

User question:
{question}

Give a clear and concise answer.
"""

    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    print("Ticket Summary:")
    print(get_summary())

    print("\nCritical tickets:")
    print(get_priority_count("Critical"))

    print("\nAverage Technical rating:")
    print(get_category_average_rating("Technical"))

    print("\nAI Test:")
    print(ask_gemini("Give me a short summary of the support tickets."))
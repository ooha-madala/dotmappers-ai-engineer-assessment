import pandas as pd


def load_data():
    df = pd.read_csv("data/support_tickets.csv")

    df["created_at"] = pd.to_datetime(df["created_at"])

    return df


if __name__ == "__main__":
    df = load_data()

    print("Dataset loaded successfully!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 tickets:")
    print(df.head())
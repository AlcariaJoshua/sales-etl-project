import pandas as pd


def transform_data(df):

    print("=" * 50)
    print("STEP 2 - TRANSFORM")
    print("=" * 50)

    print(f"Original Rows: {len(df)}")

    # Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"Duplicates Removed: {before-after}")

    # Remove missing values
    before = len(df)
    df = df.dropna()
    after = len(df)

    print(f"Missing Rows Removed: {before-after}")

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Convert numeric columns
    df["price"] = pd.to_numeric(df["price"])

    df["quantity"] = pd.to_numeric(df["quantity"])

    # Calculate revenue
    df["revenue"] = df["price"] * df["quantity"]

    # Rename date column
    df.rename(columns={"date": "order_date"}, inplace=True)

    print("Transformation Complete.")

    print(df.head())

    return df
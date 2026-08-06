import pandas as pd
from pathlib import Path


def extract_data(file_path):
    """
    Reads a CSV file and returns a Pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)

        print("✅ File loaded successfully.")
        print(f"Rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")

        return df

    except FileNotFoundError:
        print(f"❌ CSV file not found: {file_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

    return None


if __name__ == "__main__":
    # Project root
    BASE_DIR = Path(__file__).resolve().parent.parent

    # data/sales_january.csv
    csv_file = BASE_DIR / "data" / "sales_january.csv"

    dataframe = extract_data(csv_file)

    if dataframe is not None:
        print(dataframe.head())
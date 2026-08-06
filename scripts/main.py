from pathlib import Path

from extract import extract_data
from transform import transform_data
from load import load_data


def main():

    print("=" * 60)
    print("SALES ETL PIPELINE")
    print("=" * 60)

    csv_file = Path(__file__).resolve().parent.parent / "data" / "sales_january.csv"

    # Extract
    df = extract_data(csv_file)

    if df is None:
        print("Extraction failed.")
        return

    # Transform
    clean_df = transform_data(df)

    # Load
    load_data(clean_df)

    print("=" * 60)
    print("PIPELINE FINISHED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()
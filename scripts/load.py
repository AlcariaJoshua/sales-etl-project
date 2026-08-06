import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def load_data(df):
    """
    Load a transformed DataFrame into the sales table.
    """

    try:
        df.to_sql(
            name="sales",
            con=engine,
            if_exists="append",
            index=False,
        )

        print(f"Successfully loaded {len(df)} rows into the sales table.")

    except Exception as e:
        print(f"Error loading data: {e}")
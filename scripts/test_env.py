import os
from dotenv import load_dotenv
from pathlib import Path

# Build the path to the .env file
env_path = Path(__file__).resolve().parent.parent / ".env"

# Load the variables
load_dotenv(env_path)

print("Host:", os.getenv("DB_HOST"))
print("Port:", os.getenv("DB_PORT"))
print("Database:", os.getenv("DB_NAME"))
print("User:", os.getenv("DB_USER"))
print("Password:", os.getenv("DB_PASSWORD"))
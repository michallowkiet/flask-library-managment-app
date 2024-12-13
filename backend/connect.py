import psycopg2
from config import load_config


def connect(config):
    """Connect to the PostgreSQL database."""
    try:
        with psycopg2.connect(**config) as connection:
            print("Connected to the PostgreSQL database.")
            return connection
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error connecting to the PostgreSQL database: {error}")
        return None


if __name__ == "__main__":
    config = load_config()
    connect(config)

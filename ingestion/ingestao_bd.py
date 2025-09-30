import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

df = pd.read_csv("netflix_titles.csv")
data_tuples = [tuple(x) for x in df.to_numpy()]

query = """
INSERT INTO netflix_titles 
(show_id, "type", title, director, "cast", country, date_added, release_year, rating, duration, listed_in, description)
VALUES %s
ON CONFLICT (show_id) DO UPDATE SET
    "type" = EXCLUDED."type",
    title = EXCLUDED.title,
    director = EXCLUDED.director,
    "cast" = EXCLUDED."cast",
    country = EXCLUDED.country,
    date_added = EXCLUDED.date_added,
    release_year = EXCLUDED.release_year,
    rating = EXCLUDED.rating,
    duration = EXCLUDED.duration,
    listed_in = EXCLUDED.listed_in,
    description = EXCLUDED.description;
"""

with psycopg2.connect(
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    dbname=DBNAME
) as conn:
    with conn.cursor() as cursor:
        execute_values(cursor, query, data_tuples)

print("CSV sincronizado com Supabase Postgres")

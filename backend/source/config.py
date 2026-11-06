import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://snippets:change-me@db:5432/snippets")

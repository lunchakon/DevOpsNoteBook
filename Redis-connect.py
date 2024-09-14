import pandas as pd
import redis

# Replace with your actual connection details
redis_uri = "redis://xxxx:xxxx@tcredis-live.test-test.com:6379"
redis_db = 73
key_name = "REACTOR:live-2:FILE-CONTENTS"

# Connect to Redis
redis_client = redis.Redis.from_url(redis_uri, db=redis_db)

# Get the file contents from Redis
file_contents = redis_client.get(key_name).decode("utf-8")  # Decode bytes to string

# Check if the key exists and contents are not empty
if file_contents:
    # Try parsing the file contents as CSV
    try:
        df = pd.read_csv(pd.io.common. StringIO(file_contents))
        print("Successfully downloaded data into a DataFrame.")
    except pd.errors.ParserError:
        print("Error: Could not parse data as CSV. Consider using a different parsing method or checking the file format.")
else:
    print("Error: Key not found or empty contents.")

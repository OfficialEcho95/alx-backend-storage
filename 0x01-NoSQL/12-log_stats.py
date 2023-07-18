#!/usr/bin/env python3
""" Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


def log_stats():
    """ Database: logs
    """


# Connect to the MongoDB server
client = MongoClient()

# Access the logs database
db = client.logs

# Access the nginx collection
collection = db.nginx

# Count the total number of logs
total_logs = collection.count_documents({})

print(f"{total_logs} logs")

# Count the number of logs for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"    method {method}: {count}")

# Count the number of logs with method=GET and path=/status
status_check_count = collection.count_documents(
    {"method": "GET", "path": "/status"})
print(f"{status_check_count} status check")

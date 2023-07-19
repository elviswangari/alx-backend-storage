#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB,
including the top 10 most present IPs.
"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Displays stats about Nginx logs stored in MongoDB,
    including the top 10 most present IPs.
    """
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    number_of_gets = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{number_of_gets} status check")
    # Top 10 IPs
    top_ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    top_ips = list(top_ips)
    top_ips = sorted(top_ips, key=lambda x: x['count'], reverse=True)
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(mongo_collection)

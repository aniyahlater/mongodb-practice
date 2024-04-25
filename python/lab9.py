#!/usr/bin/env python3

from pymongo import MongoClient, errors
import os
from db import *
db=client.ybf3jw
#creating a new collection
    #use studioghibli
#inserting 5 documents
db.studioghibli.insert_many([
    {"Title": "The Boy and the Heron", "releasedate":2023, "movielength":124, "rating": "PG-13", "oscarnom": "Yes"},
    {"Title":"The Wind Rises", "releasedate":2013, "movielength":126, "rating": "PG-13", "oscarnom": "Yes"},
    {"Title":"Ponyo", "releasedate":2008, "movielength":101, "rating": "G", "oscarnom": "No"},
    {"Title":"Howl's Moving Castle", "releasedate":2004, "movielength":119, "rating":"PG", "oscarnom": "Yes"},
    {"Title":"Spirited Away", "releasedate":2001, "movielength":125, "rating": "PG", "oscarnom":"Yes"},
    {"Title":"Princess Mononoke", "releasedate":1997, "movielength":134, "rating": "PG-13", "oscarnom":"Yes"}
])
# going to write a query that only shows three different results
results = db.studioghibli.find({"rating":"PG-13"})
for result in results:
    print(result)
    
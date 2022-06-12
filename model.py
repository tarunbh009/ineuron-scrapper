import pymongo
def connection(uri: str):

    client = pymongo.MongoClient(uri)
    database = client["fsds-scrapper"]
    course_collection = database["course"]
    return course_collection

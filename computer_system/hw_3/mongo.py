import argparse
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# Connect to MongoDB
uri = "mongodb://localhost:27017"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.HW3

parser = argparse.ArgumentParser(description="Manage cats in the database")
parser.add_argument(
    "--action", help="[create, read, update, delete, find_by_name, update_age_by_name, add_feature, delete_by_name, delete_all]")
parser.add_argument("--id", help="ID of the cat (for specific actions)")
parser.add_argument("--name", help="Name of the cat")
parser.add_argument("--age", type=int,
                    help="Age of the cat (for creating or updating age)")
parser.add_argument("--features", nargs="+",
                    help="Features of the cat (list of features)")
parser.add_argument("--new_feature", help="New feature to add to the cat")

args = vars(parser.parse_args())
action = args.get("action")
pk = args.get("id")
name = args.get("name")
age = args.get("age")
features = args.get("features")
new_feature = args.get("new_feature")


def read():
    cats = db.cats.find()
    return list(cats)


def create(name, age, features):
    return db.cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })

def update(pk, name, age, features):
    return db.cats.update_one({"_id": ObjectId(pk)}, {"$set": {"name": name, "age": age, "features": features}})

def delete(pk):
    return db.cats.delete_one({"_id": ObjectId(pk)})

def find_cat_by_name(name):
    cat = db.cats.find_one({"name": name})
    if cat:
        return cat
    else:
        return "No cat found with that name."

def update_cat_age_by_name(name, new_age):
    result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    return result.modified_count

def add_feature_to_cat(name, new_feature):
    result = db.cats.update_one(
        {"name": name}, {"$addToSet": {"features": new_feature}})
    return result.modified_count


def delete_cat_by_name(name):
    result = db.cats.delete_one({"name": name})
    return result.deleted_count


def delete_all_cats():
    result = db.cats.delete_many({})
    return result.deleted_count


if __name__ == "__main__":
    match action:
        case "create":
            r = create(name, age, features)
            print(f"Inserted ID: {r.inserted_id}")
        case "read":
            cats = read()
            for cat in cats:
                print(cat)
        case "find_by_name":
            cat_info = find_cat_by_name(name)
            print(cat_info)
        case "update":
            r = update(pk, name, age, features)
            print(f"Modified count: {r.modified_count}")
        case "update_age_by_name":
            modified_count = update_cat_age_by_name(name, age)
            print(f"Modified count: {modified_count}")
        case "add_feature":
            modified_count = add_feature_to_cat(name, new_feature)
            print(f"Modified count: {modified_count}")
        case "delete":
            r = delete(pk)
            print(f"Deleted count: {r.deleted_count}")
        case "delete_by_name":
            deleted_count = delete_cat_by_name(name)
            print(f"Deleted count: {deleted_count}")
        case "delete_all":
            deleted_count = delete_all_cats()
            print(f"Deleted count: {deleted_count}")
        case _:
            print("Wrong action")
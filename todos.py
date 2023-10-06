import argparse
from datetime import datetime

import pymongo
from bson import ObjectId
from bson.errors import InvalidId

db_client = pymongo.MongoClient(
    "mongodb://root:mySecureDbPassword1!@localhost:27017/"  # noqa: E501
)
db = db_client["myAppDb"]


def get_todos() -> None:
    """
    Get Todos
    """
    print()
    for document in db.todos.find({"completed": False}):
        for key, value in document.items():
            print(f"{key}: {value}")
        print()

    return None


def create_todo(title: str) -> None:
    """
    Create a todo
    """
    create_result = db.todos.insert_one(
        {"title": title, "completed": False, "created_date": datetime.utcnow()}
    )
    print(f"New Todo ID: {create_result.inserted_id}")

    return None


def complete_todo(todo_id: str) -> None:
    """
    Complete a todo
    """
    try:
        todo_object_id = ObjectId(todo_id)
    except InvalidId:
        print("Invalid Todo Id")
        return None

    update_result = db.todos.update_one(
        {"_id": todo_object_id}, {"$set": {"completed": True}}
    )

    if update_result.matched_count == 0:
        print("Todo not found")
    else:
        print("Completed todo, nice work! 🎉")

    return None


def delete_todo(todo_id: str) -> None:
    """
    Delete a todo
    """
    try:
        todo_object_id = ObjectId(todo_id)
    except InvalidId:
        print("Invalid Todo Id")
        return None

    delete_result = db.todos.delete_one({"_id": todo_object_id})

    if delete_result.deleted_count == 0:
        print("Todo not found")
    else:
        print("Deleted the todo")

    return None


def main() -> None:
    """
    Mongo todo CRUD Operations
    """
    parser = argparse.ArgumentParser(description="Mongo CRUD Operations")
    parser.add_argument(
        "-o",
        "--operation",
        choices=["create", "read", "complete", "delete"],
        default="read",
        help="Choose CRUD Operation",
    )
    parser.add_argument(
        "-d",
        "--data",
        help="New todo title or ID of existing todo",
    )
    args = parser.parse_args()

    if args.operation == "read":
        get_todos()
    elif args.operation == "create":
        if not args.data:
            print("Provide the new todo title with the '-d' flag")
            return None

        create_todo(title=args.data)
    elif args.operation == "complete":
        if not args.data:
            print("Provide the todo id with the '-d' flag")
            return None

        complete_todo(todo_id=args.data)
    elif args.operation == "delete":
        if not args.data:
            print("Provide the todo id with the '-d' flag")
            return None

        delete_todo(todo_id=args.data)

    return None


if __name__ == "__main__":
    main()

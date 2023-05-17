from flask import jsonify, request
from messages.models import MessageModel
from messages.api.serializers import MessageSchema

def hello_world():
    return jsonify({"message": "Hello World from messages"})

def get_messages():
    messages = MessageModel.query.all()
    schema = MessageSchema(many=True).dump(messages)
    grouped_messages = MessageSchema.group_by_email(schema)

    return jsonify({"messages": grouped_messages})

def create_message():
    if request.method == "POST":
        data = request.get_json()
        message = MessageModel(
            name = data["name"],
            email = data["email"],
            subject = data["subject"],
            message = data["message"]
        ).save()

        return jsonify({"message": "Done"})
from databases.extensions.init_ext import ma_serializer
from marshmallow import fields


class MessageSchema(ma_serializer.Schema):
    name = fields.String(required=True)
    subject = fields.String(required=True)
    message = fields.String(required=True)
    email = fields.Email(required=True)

    # solucionar esto del resultado 
    @staticmethod
    def group_by_email(messages):
        result = {}
        for message in messages:
            email = message["email"]
            if email not in result:
                result[email] = []
            result[email].append(
                {"name": message["name"], "subject": message["subject"], "message": message["message"]}
            )
        return [
            {"email": email, "messages": messages} for email, messages in result.items()
        ]

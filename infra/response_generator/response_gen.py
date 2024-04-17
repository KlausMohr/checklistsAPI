from flask import Response
import json

def response_gen(status, content_type, content, message=False):
        body = {}
        body[content_type] = content
        if message:
            body["message"] = message
        return Response(json.dumps(body), status=status, mimetype="application/json")

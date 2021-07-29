from functools import wraps
import secrets
from flask import request, jsonify, json
import decimal

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            #Convert decimal instances into strings
            return str(obj)
        return super(JSONEncoder,self).default(obj)
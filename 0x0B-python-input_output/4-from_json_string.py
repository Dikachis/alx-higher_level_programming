#!/usr/bin/python3
"""
The "from_json_string" function container
"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)

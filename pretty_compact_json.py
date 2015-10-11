#!/usr/bin/env python3

import sys
import json
from collections import OrderedDict


def format_json(obj, indentation=2):
    indent = ' ' * indentation
    if isinstance(obj, list):
        print('[')
        for item in obj[:-1]:
            print('{}{},'.format(indent, json.dumps(item)))
        if len(obj) > 0:
            print('{}{}'.format(indent, json.dumps(obj[-1])))
        print(']')
    elif isinstance(obj, dict):
        print('{')
        items = list(obj.items())
        for key, val in items[:-1]:
            print('{}"{}": {},'.format(indent, key, json.dumps(val)))
        if len(items) > 0:
            key, val = items[-1]
            print('{}"{}": {}'.format(indent, key, json.dumps(val)))
        print('}')
    else:
        print(json.dumps(obj))


def format_file(file):
    for line in file:
        # OrderedDict to preserve key ordering in objects
        obj = json.loads(line, object_pairs_hook=OrderedDict)
        format_json(obj)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        with open(filename) as f:
            format_file(f)
    else:
        format_file(sys.stdin)

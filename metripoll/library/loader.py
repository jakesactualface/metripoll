import json

def __get_json_text(uri):
  # TODO: support http requests
  with open(uri, 'r') as input:
    return input.read()

def load_json(uri):
  return json.loads(__get_json_text(uri))
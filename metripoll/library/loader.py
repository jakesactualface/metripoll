import json

def __get_json_text(uri) -> str:
  # TODO: support http requests
  with open(uri, 'r') as input:
    return input.read()

def load_json(uri) -> dict:
  return json.loads(__get_json_text(uri))
import json

def __getJsonText(uri):
  # TODO: support http requests
  with open(uri, 'r') as input:
    return input.read()

def loadjson(uri):
  return json.loads(__getJsonText(uri))
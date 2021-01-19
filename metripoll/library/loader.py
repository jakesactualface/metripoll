import requests

def load_json(uri) -> dict:
  return requests.get(uri).json()
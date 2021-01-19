import sys

from . import library

def runnable():
  json_metrics = sys.argv[1:]

  print("Supplied arguments: {}".format(json_metrics))

  json_object = library.loader.loadjson('data/mockResponse.json')

  for metric in json_metrics:
    target = library.parser.parse(json_object, metric)
    print("{} = {}".format(metric, target))
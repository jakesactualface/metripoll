from metripoll.library.poller import Poller
import sys

from . import library

def runnable():
  params = library.parser.parse_params(sys.argv[1:])

  json_metrics = params["metrics"]

  json_object = library.loader.load_json('data/mockResponse.json')

  poller = Poller(params)

  for metric in json_metrics:
    target = library.parser.parse_metrics(json_object, metric)
    print("{} = {}".format(metric, target))
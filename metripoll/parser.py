from typing import Text
from metripoll.metric import Metric


def __getMemberValue(target: dict, member: Text):
  # TODO: also handle arrays
  return target[member]

def parse_metrics(object: dict, metric: Metric):
  target = object

  # TODO: also handle arrays

  for member in metric.get_path_list():
    target = __getMemberValue(target, member)
  
  return target
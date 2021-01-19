from metripoll.library.parser import parse_metrics
from metripoll.library.loader import load_json
from metripoll.library.pollconfig import PollConfig

class Poller:
  def __init__(self, config: PollConfig):
    self.config = config
    self.headers = config.metrics
    self.data = {}
  
  def start(self):
    # TODO: loop after each interval
    self.retrieve_metrics()

    if len(self.config.output) > 0:
      print(self.get_header())
      print(self.get_data_row())
    else:
      # TODO: output to file
      return

  def retrieve_metrics(self):
    object = load_json(self.config.input)

    for metric in self.headers:
      target = parse_metrics(object, metric)
      self.data[metric] = target
  
  def get_header(self):
    return ",".join(self.headers)
  
  def get_data_row(self):
    data_row = []

    for header in self.headers:
      data_row.append(self.data[header])

    return ",".join(data_row)
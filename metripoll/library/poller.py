from metripoll.library.parser import parse_metrics
from metripoll.library.loader import load_json
from metripoll.library.pollconfig import PollConfig
import time

class Poller:
  def __init__(self, config: PollConfig):
    self.config = config
    self.headers = config.metrics
    self.data = {}
  
  def start(self):
    self.print_header_row()

    try:
      while True:
        self.retrieve_metrics()
        self.print_new_row()
        time.sleep(self.config.interval)
    except KeyboardInterrupt:
      print("Exit code received. Polling terminated.")

  def print_header_row(self):
    if self.config.fileoutput:
      with open(self.config.output, 'w') as writer:
        writer.write(self.get_header())
    else:
      print(self.get_header())

  def print_new_row(self):
    if self.config.fileoutput:
      with open(self.config.output, 'a') as writer:
        writer.write("\n{}".format(self.get_data_row()))
    else:
      print(self.get_data_row(), flush=True)

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
      data_row.append("{}".format(self.data[header]))

    return ",".join(data_row)
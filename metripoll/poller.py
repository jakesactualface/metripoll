from metripoll.parser import parse_metrics
from metripoll.loader import load_json
from metripoll.configuration import Configuration
import datetime
import time

class Poller:
  def __init__(self, config: Configuration):
    self.config = config
    self.headers = config.get_headers()
    self.data = {}
  
  def start(self):
    self.print_header_row()

    try:
      while True:
        self.retrieve_metrics()
        self.print_new_row()
        time.sleep(self.config.get_interval())
    except KeyboardInterrupt:
      print("Exit code received. Polling terminated.")

  def print_header_row(self):
    self.config.output(self.get_header())

  def print_new_row(self):
    self.config.output(self.get_data_row())

  def retrieve_metrics(self):
    object = load_json(self.config.get_input())

    for metric in self.config.get_metrics():
      target = parse_metrics(object, metric)
      self.data[metric] = target
  
  def get_header(self):
    return ",".join(self.headers)
  
  def get_data_row(self):
    data_row = []

    if self.config.is_timestamp_enabled():
      data_row.append(str(datetime.datetime.now()))

    for metric in self.data:
      data_row.append("{}".format(self.data[metric]))

    return ",".join(data_row)
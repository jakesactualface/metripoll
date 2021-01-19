import sys

class PollConfig:
  def __init__(self):
    self.interval = 1
    self.input = ""
    self.output = ""
    self.fileoutput = False
    self.metrics = []
  
  def verify(self):
    if len(self.input) < 1:
      print("You must supply a URL to poll for data.")
      sys.exit(2)
    else:
      print("Given URL: {}".format(self.input))
    
    if len(self.metrics) < 1:
      print("JSON metrics must be supplied as arguments.")
      sys.exit(2)
    else:
      print("Given metrics: {}".format(self.metrics))
    
    if self.interval < 1:
      print("Polling interval cannot be less than 1 second.")
      sys.exit(2)
    else:
      print("Given polling interval (seconds): {}".format(self.interval))
    
    if len(self.output) > 0:
      print("Output will be saved to file: {}".format(self.output))
      self.fileoutput = True
    else:
      print("Output will be printed to the console.")
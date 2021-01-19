class Poller:
  def __init__(self, params):
    self.interval = params["interval"]
    self.input = params["url"]
    self.output = params["output"]
    self.metrics = params["metrics"]
    print("poller: {}".format(self))
  
  def start():
    return None
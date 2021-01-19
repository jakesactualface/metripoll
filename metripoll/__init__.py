import sys

import metripoll.library as library
from metripoll.library.poller import Poller

def runnable():
  config = library.parser.parse_params(sys.argv[1:])
  poller = Poller(config)
  poller.start()
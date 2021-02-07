from metripoll.configuration import Configuration
from metripoll.poller import Poller

def main():
  config = Configuration()
  poller = Poller(config)
  poller.start()

if __name__ == "__main__":
  main()
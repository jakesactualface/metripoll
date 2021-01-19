import sys, getopt

from metripoll.library.pollconfig import PollConfig

def __getMemberValue(target, member):
  # TODO: also handle arrays
  return target[member]

def parse_metrics(object, path):
  target = object

  pathMembers = path.split('.')
  # TODO: also handle arrays

  for member in pathMembers:
    target = __getMemberValue(target, member)
  
  return target

def parse_params(arguments) -> PollConfig:
  config = PollConfig()

  try:
    opts, args = getopt.getopt(arguments, "u:o:t:")
  except getopt.GetoptError:
    print("metripoll -u <url> [-o <outputFile>] [-t <pollInterval>] {metrics...}")
    sys.exit(2)

  for opt, arg in opts:
    if opt == "-u":
      config.input = arg

    elif opt == "-o":
      config.output = arg

    elif opt == "-t":
      config.interval = int(arg)

  config.metrics = args

  return config
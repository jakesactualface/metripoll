import sys, getopt

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



def parse_params(arguments):
  params = dict()

  try:
    opts, args = getopt.getopt(arguments, "u:o:t:")
  except getopt.GetoptError:
    print("metripoll -u <url> -o <outputFile>")
    sys.exit(2)

  for opt, arg in opts:
    if opt == "-u":
      print("Given URL: {}".format(arg))
      params["url"] = arg

    elif opt == "-o":
      print("Printing to output file: {}".format(arg))
      params["output"] = arg

    elif opt == "-t":
      print("Polling at interval (seconds): {}".format(arg))
      params["interval"] = arg

  if len(args) < 1:
    print("JSON metrics must be supplied as arguments.")
    sys.exit(2)
  
  params["metrics"] = args
  print("Polling for metrics: {}".format(args))

  return params
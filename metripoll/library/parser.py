def __getMemberValue(target, member):
  # TODO: also handle arrays
  return target[member]

def parse(object, path):
  target = object

  pathMembers = path.split('.')
  # TODO: also handle arrays

  for member in pathMembers:
    target = __getMemberValue(target, member)
  
  return target
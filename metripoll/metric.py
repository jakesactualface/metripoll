from typing import List, Text

class Metric:
  def __init__(self, path_string, delimiter, alias=None):
    self.path_string = path_string
    self.path_list = path_string.split(delimiter)
    self.delimiter = delimiter
    self.alias = alias

  def get_header_string(self) -> Text:
    if self.alias is None:
      return self.path_string
    return self.alias

  def get_path_list(self) -> List[Text]:
    return self.path_list

  def get_path_string(self) -> Text:
    return self.path_string
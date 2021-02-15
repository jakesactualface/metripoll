from argparse import Namespace
import unittest
from metripoll.metric import Metric
from metripoll.configuration import Configuration

class ConfigurationTest(unittest.TestCase):

  URL = "testUrl"
  METRIC = "testMetric"
  DELIMITER = "."
  INTERVAL = 1

  def setUp(self):
    expectedMetrics = [Metric(self.METRIC, self.DELIMITER)]
    self.expectedArgs = {
      "url": self.URL,
      "interval": self.INTERVAL,
      "delimiter": self.DELIMITER,
      "metrics": expectedMetrics
    }

  # _load_config tests
  def test_emptyArgs(self):
    with self.assertRaises(SystemExit):
      Configuration._load_config(None, [])

  def test_noUrl(self):
    with self.assertRaises(SystemExit):
      Configuration._load_config(None, [self.METRIC])

  def test_noMetric(self):
    with self.assertRaises(SystemExit):
      Configuration._load_config(None, ["-u", self.URL])

  def test_minimumArguments(self):
    returnedArgs = Configuration._load_config(None, ["-u", self.URL, self.METRIC])
    self._assertArgs(self.expectedArgs, returnedArgs)

  def test_multipleMetrics(self):
    self.expectedArgs["metrics"].append(Metric("anotherMetric", self.DELIMITER))
    returnedArgs = Configuration._load_config(None, ["-u", self.URL, self.METRIC, "anotherMetric"])
    self._assertArgs(self.expectedArgs, returnedArgs)

  def test_delimiters(self):
    self.expectedArgs["metrics"] = [Metric("OuterObject~InnerObject1", "~"), Metric("OuterObject~InnerObject2", "~")]
    self.expectedArgs["delimiter"] = "~"
    returnedArgs = Configuration._load_config(None, ["-u", self.URL, "-d", "~", "OuterObject~InnerObject1", "OuterObject~InnerObject2"])
    self._assertArgs(self.expectedArgs, returnedArgs)

  def test_allStandardArguments(self):
    self.expectedArgs["timestamp"] = True
    self.expectedArgs["output"] = "exampleFile.txt"
    self.expectedArgs["interval"] = 8
    self.expectedArgs["delimiter"] = "!"
    returnedArgs = Configuration._load_config(None, ["-u", self.URL, self.METRIC, "-t", "-o", "exampleFile.txt", "-i", "8", "-d", "!"])
    self._assertArgs(self.expectedArgs, returnedArgs)

  # helper methods
  def _assertArgs(self, expected: dict, actual: Namespace):
    self.assertEquals(expected["url"], actual.url)
    self.assertEquals(expected["interval"], actual.interval)
    self.assertEquals(expected["delimiter"], actual.delimiter)
    self._assertMetrics(expected["metrics"], actual.metrics)

  def _assertMetrics(self, expectedList: list[Metric], actualList: list[Metric]):
    for expected, actual in zip(expectedList, actualList):
      self.assertEquals(expected.alias, actual.alias)
      self.assertEquals(expected.delimiter, actual.delimiter)
      self.assertEquals(expected.path_string, actual.path_string)
      self.assertEquals(expected.path_list, actual.path_list)

if __name__ == '__main__':
    unittest.main()
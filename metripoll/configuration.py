import argparse
from typing import List, Text
from metripoll.metric import Metric
from importlib.metadata import version


class Configuration:
    def __init__(self):
        self.arguments = self._load_config()

    def _load_config(self):
        parser = argparse.ArgumentParser(prog="metripoll")
        parser.add_argument('--version', action='version', version=version("metripoll"))
        parser.add_argument(
            "-u", "--url", help="URL to poll for metrics", required=True)
        parser.add_argument(
            "-i", "--interval", help="Polling interval in seconds", default=1, type=int)
        parser.add_argument("-o", "--output", help="Output file name")
        parser.add_argument(
            "-d", "--delimiter", help="Delimiter character to use for parsing metrics", default=".")
        parser.add_argument(
            "-t", "--timestamp", help="Include timestamps in polling output", action="store_true")
        parser.add_argument(
            "metrics", help="JSON metrics to be parsed from the response", nargs="+", action=MetricParseAction)

        return parser.parse_args()

    def get_metrics(self) -> List[Metric]:
        return self.arguments.metrics

    def get_input(self) -> Text:
        return self.arguments.url

    def get_interval(self) -> int:
        return self.arguments.interval

    def is_timestamp_enabled(self) -> bool:
        return self.arguments.timestamp

    def get_headers(self) -> List[Text]:
        headers = []
        if self.is_timestamp_enabled():
            headers.append("Timestamp")
        for metric in self.get_metrics():
            headers.append(metric.get_header_string())
        return headers

    def output(self, text):
        if self.arguments.output is None:
            print(text, flush=True)
        else:
            with open(self.arguments.output, 'a') as writer:
                writer.write("{}\n".format(text))


class MetricParseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        namespace.metrics = []
        for value in values:
            namespace.metrics.append(Metric(value, namespace.delimiter))

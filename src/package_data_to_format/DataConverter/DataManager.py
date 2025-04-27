import csv
import json
import os.path

import pandas as pd
import xmltodict

import src.package_data_to_format.decor.singletone


@src.package_data_to_format.decor.singletone.singleton
class ReturningData:
    datapayload: str = None
    state: str = None

    def __init__(self, path_to_file):
        self.path = path_to_file
        self._getExt()

    def _getJSON(self):
        f = open(self.path, "r")
        self.datapayload = f.read()
        self.state = "ok"

    def _getXML(self):
        f = open(self.path, "r")

        o = xmltodict.parse(f.read())  # https://stackoverflow.com/questions/191536/converting-xml-to-json-using-python
        self.datapayload = json.dumps(o)  # '{"e": {"a": ["text", "text"]}}'
        self.state = "ok"

    def _getCSV(self):
        csv_file = pd.DataFrame(pd.read_csv(self.path, sep=",", header=0, index_col=False))
        self.datapayload = csv_file.to_json(orient="records", date_format="epoch", double_precision=10,
                                            force_ascii=True, date_unit="ms", default_handler=None)
        self.state = "ok"

    def _getExt(self):
        self.ext = os.path.splitext(self.path)[1]

    def _unsupported(self):
        self.state = "unsupported"
        self.datapayload = "usupported"
        self.state = "ok"

    def get_data_formatJSON(self) -> json:
        match self.ext:
            case ".json":
                self._getJSON()
            case ".csv":
                self._getCSV()
            case ".xml":
                self._getXML()
            case _:
                self._unsupported()
        from_to_return = {
            "dataPayload": self.datapayload,
            "state": self.state
        }
        return json.dumps(from_to_return)

    def get_data_formatXML(self) -> json:
        f = open(self.path)
        csv_f = csv.reader(f)
        data = []

        for row in csv_f:
            data.append(row)
        f.close()
        self.datapayload = str(data)
        fromToReturn = {
            "dataPayload": self.datapayload,
            "state": self.state
        }
        return json.dumps(fromToReturn)

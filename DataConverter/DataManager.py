import csv
import json
import os.path

import pandas as pd
import xmltodict

import decor.singletone


@decor.singletone.singleton
class ReturningData:
    datapayload: str = None
    state: str = None
    fromToReturn = {
        "dataPayload": datapayload,
        "state": state
    }

    def __init__(self, path_to_file):
        self.path = path_to_file
        self._getExt()
        None

    def _getJSON(self):
        f = open(self.path, "r")
        self.datapayload = f.read()
        # os.path.getsize('path_to_your_file')
        # print('Размер файла:', file_size, 'байт')
        self.state = "ok"
        None

    def _getXML(self):
        f = open(self.path, "r")

        o = xmltodict.parse(f.read())  # https://stackoverflow.com/questions/191536/converting-xml-to-json-using-python
        self.datapayload = json.dumps(o)  # '{"e": {"a": ["text", "text"]}}'
        self.state = "ok"
        None

    def _getCSV(self):
        csv_file = pd.DataFrame(pd.read_csv(self.path, sep=",", header=0, index_col=False))
        self.datapayload = csv_file.to_json(orient="records", date_format="epoch", double_precision=10,
                                            force_ascii=True, date_unit="ms", default_handler=None)
        self.state = "ok"

    def _getExt(self):
        self.ext = os.path.splitext(self.path)[1]

    def _unsupported(self):
        self.state = "unsupported"
        self.datapayload = json.dumps(self.fromToReturn)
        self.state = "ok"

    def getDataFormatJSON(self) -> json:
        match self.ext:
            case ".json":
                self._getJSON()
            case ".csv":
                self._getCSV()
            case ".xml":
                self._getXML()
            case _:
                self._unsupported()
        return json.dumps(self.fromToReturn)

    def getDataFormatXML(self) -> json:
        f = open(self.path)
        csv_f = csv.reader(f)
        data = []

        for row in csv_f:
            data.append(row)
        f.close()
        self.datapayload = str(data)

        return json.dumps(self.fromToReturn)

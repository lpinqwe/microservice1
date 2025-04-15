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


    def __init__(self, path_to_file): #todo неформатированный код
        self.path = path_to_file
        self._getExt()
        None

    def _getJSON(self):
        f = open(self.path, "r")
        self.datapayload = f.read()
        # os.path.getsize('path_to_your_file') #todo коментарии старого кода без туду и описания зачем оставлен
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
        self.datapayload = "usupported"
        self.state = "ok"

    def getDataFormatJSON(self) -> json: #todo несоблюдение конвенции
        match self.ext:
            case ".json":
                self._getJSON()
            case ".csv":
                self._getCSV()
            case ".xml":
                self._getXML()
            case _:
                self._unsupported()
        fromToReturn = { #todo несоблюдение конвенции
            "dataPayload": self.datapayload,
            "state": self.state
        }
        return json.dumps(fromToReturn)

    def getDataFormatXML(self) -> json: #todo несоблюдение конвенции
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

import json

from _distutils_hack import override

from src.package_data_to_format.DataConverter.DataManager import ReturningData
from src.package_data_to_format.interfaces import messagesInterface
from src.package_data_to_format.interfaces.CommandStructure import Command

class CommandGetXML(messagesInterface.MessageInterface):
    """
    CommandGetJSON: команда для возврата данных в формате XML.

    Описание:
    - Принимает объект команды (`mapa`).
    - Обрабатывает данные и возвращает их в формате XML.
    """
    def __init__(self, mapa):
        super().__init__(mapa)
        pass

    def execute(self) -> Command:
        # print(self.command)
        # oroginal command ->self.command
        tmp: ReturningData = ReturningData()
        tmp.get_data_formatXML()
        self.command.msgPayload = tmp.datapayload
        answer = self.command
        return answer

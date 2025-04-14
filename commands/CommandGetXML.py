import json

from _distutils_hack import override

from DataConverter.DataManager import ReturningData
from interfaces import messagesInterface
from interfaces.CommandStructure import Command

class CommandGetXML(messagesInterface.MessageInterface):

    def __init__(self, mapa):
        """***this command will return XML format from data***"""
        super().__init__(mapa)
        pass

    def execute(self) -> Command:
        # print(self.command)
        # oroginal command ->self.command
        tmp: ReturningData = ReturningData()
        tmp.getDataFormatXML()
        self.command.msgPayload = tmp.datapayload
        answer = self.command
        return answer

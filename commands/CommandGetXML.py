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
        #oroginal command ->self.command
        tmp:ReturningData = ReturningData()
        self.command.msgPayload=tmp.getDataFormatXML()
        answer = Command(tmp)

        return answer

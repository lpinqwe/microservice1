
import json
import os

from _distutils_hack import override

from DataConverter.DataManager import ReturningData
from interfaces.CommandStructure import Command
from interfaces import messagesInterface
class TestCommand(messagesInterface.MessageInterface):


    def __init__(self, map):
        """***this command will return TEST ***"""
        super().__init__(map)
        print(map)

        pass

    def execute(self) -> Command:
        # print(self.command)
        # oroginal command ->self.command
        tmp: ReturningData = ReturningData()
        tmp.getDataFormatXML()
        self.command.msgPayload = tmp.datapayload
        answer = self.command
        return answer

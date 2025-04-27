
import json
import os

from _distutils_hack import override
from  utils.Logger import LoggerAll as log
from DataConverter.DataManager import ReturningData
from interfaces.CommandStructure import Command
from interfaces import messagesInterface
class TestCommand(messagesInterface.MessageInterface):
    """***this command will return TEST ***"""

    def __init__(self, map):
        super().__init__(map)
        #print(map)
        log.logger.info(map)
        pass

    def execute(self) -> Command:
        # print(self.command)
        # oroginal command ->self.command
        tmp: ReturningData = ReturningData()
        tmp.get_data_formatXML()
        self.command.msgPayload = tmp.datapayload
        answer = self.command
        return answer

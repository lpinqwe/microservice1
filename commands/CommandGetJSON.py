from DataConverter.DataManager import ReturningData
from interfaces import messagesInterface
from interfaces.CommandStructure import Command
from interfaces.CommandStructure import Command


class CommandGetJSON(messagesInterface.MessageInterface):

    def __init__(self, mapa:Command):

        """***this command will return json format from data***"""
        super().__init__(mapa)
        pass

    def execute(self) -> Command:
        #print(self.command)
        #oroginal command ->self.command
        tmp:ReturningData = ReturningData()
        tmp.getDataFormatJSON()
        self.command.msgPayload=tmp.datapayload
        answer = self.command
        return answer

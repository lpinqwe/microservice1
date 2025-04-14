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
        #oroginal command ->self.command
        tmp:ReturningData = ReturningData()
        self.command.msgPayload=tmp.getDataFormatJSON()
        answer = Command(tmp)

        return answer

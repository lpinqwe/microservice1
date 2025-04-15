from DataConverter.DataManager import ReturningData
from interfaces import messagesInterface
from interfaces.CommandStructure import Command #todo импотры лишние
from interfaces.CommandStructure import Command


class CommandGetJSON(messagesInterface.MessageInterface):

    def __init__(self, mapa:Command):

        """***this command will return json format from data***""" #todo описание уровня класса
        super().__init__(mapa)
        pass

    def execute(self) -> Command:
        #print(self.command)
        #oroginal command ->self.command#todo комменты
        tmp:ReturningData = ReturningData()
        tmp.getDataFormatJSON()
        self.command.msgPayload=tmp.datapayload #todo форматирование
        answer = self.command
        return answer

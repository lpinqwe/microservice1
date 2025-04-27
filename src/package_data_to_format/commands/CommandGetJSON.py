from src.package_data_to_format.DataConverter.DataManager import ReturningData
from src.package_data_to_format.interfaces import messagesInterface
from src.package_data_to_format.interfaces.CommandStructure import Command


class CommandGetJSON(messagesInterface.MessageInterface):
    """
    CommandGetJSON: команда для возврата данных в формате JSON.

    Описание:
    - Принимает объект команды (`mapa`).
    - Обрабатывает данные и возвращает их в формате JSON.
    """
    def __init__(self, mapa:Command):

        super().__init__(mapa)
        pass

    def execute(self) -> Command:
        tmp:ReturningData = ReturningData()
        tmp.get_data_formatJSON()
        self.command.msgPayload=tmp.datapayload #todo форматирование
        answer = self.command
        return answer

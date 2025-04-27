from src.package_data_to_format.DataConverter.DataManager import ReturningData
from src.package_data_to_format.interfaces import messagesInterface
from src.package_data_to_format.interfaces.CommandStructure import Command
from src.package_data_to_format.utils.Logger import LoggerAll as log


class TestCommand(messagesInterface.MessageInterface):
    """***this command will return TEST ***"""

    def __init__(self, map):
        super().__init__(map)
        # print(map)
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

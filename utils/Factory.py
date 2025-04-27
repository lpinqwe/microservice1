from commands.CommandGetJSON import CommandGetJSON
from commands.CommandGetXML import CommandGetXML
from commands.TestCommand import TestCommand
from interfaces.CommandStructure import Command
from utils.Logger import LoggerAll as log


class Factory:
    def __init__(self):
        CMD_GET_JSON = 'getjson'
        CMD_GET_XML = 'getxml'
        CMD_TEST = 'test'

        self.commands = {
            CMD_GET_JSON: CommandGetJSON,
            CMD_GET_XML: CommandGetXML,
            CMD_TEST: TestCommand

        }

    def execute_command(self, command: Command) -> Command:
        try:
            cmd = command.msgCommand.lower()
            command_to_execute = self.commands.get(cmd)

            if command_to_execute is None:
                raise ValueError(f"Unknown command type: {command_to_execute}")
            if not callable(command_to_execute):
                raise TypeError(f"Command {command_to_execute} is not callable.")
            cmd_obj = command_to_execute(command)
            return cmd_obj.execute()

        except Exception as e:
            log.logger.exception(Command)
            log.logger.exception("sthGoneWrong")
            log.logger.exception(e)

            raise e

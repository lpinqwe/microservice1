import json
from abc import abstractmethod,ABC
from src.package_data_to_format.interfaces.CommandStructure import Command
class MessageInterface(ABC):


    @abstractmethod
    def __init__(self,command_to_process:Command):
        self.command:Command=command_to_process
        return


    @abstractmethod
    def execute(self)->Command:
        return

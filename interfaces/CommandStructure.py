import json
from dataclasses import dataclass

from utils.Logger import LoggerAll as log


@dataclass
class Command:
    msgID: str
    msgPayload: str
    msgCommand: str
    #command example
    # {
    # "msgCommand":"",
    # "msgID":"".
    # "msgPayload":""
    # }
    CMD_msg_ID = 'msgID'
    CMD_msg_payload = 'msgPayload'
    CMD_command = 'msgCommand'

    def __init__(self, string_format_command):
        log.logger.info(f"Попытка разобрать команду: {string_format_command}")
        data = json.loads(string_format_command)
        self.msgCommand = data['msgCommand']
        self.msgID = data['msgID']
        self.msgPayload = data['msgPayload']

    def get(self):
        map = {
            self.CMD_msg_ID: self.msgID,
            self.CMD_msg_payload: self.msgPayload,
            self.CMD_command: self.msgCommand
        }
        return json.dumps(map)

    def __str__(self):
        map = {
            'msgID': self.msgID,
            'msgPayload': self.msgPayload,
            'msgCommand': self.msgCommand
        }
        return str(map)

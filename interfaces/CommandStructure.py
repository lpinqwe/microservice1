from dataclasses import dataclass
import json

@dataclass
class Command:
    msgID: str
    msgPayload: str
    msgCommand: str
    #{
    #"msgCommand":"",
    #"msgID":"".
    #"msgPayload":""
    # }
    def __init__(self, string_format_command):
        print(f"Попытка разобрать команду: {string_format_command}")  # Логируем строку

        data = json.loads(string_format_command)
        self.msgCommand=data['msgCommand']
        self.msgID = data['msgID']
        self.msgPayload = data['msgPayload']
    def get(self):
        map = {
            'msgID': self.msgID,
            'msgPayload': self.msgPayload,
            'msgCommand': self.msgCommand
        }
        return json.dumps(map)

    def __str__(self):
        map = {
            'msgID': self.msgID,
            'msgPayload': self.msgPayload,
            'msgCommand': self.msgCommand
        }
        return str(map)
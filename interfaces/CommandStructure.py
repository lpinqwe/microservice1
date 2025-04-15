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
        print(f"Попытка разобрать команду: {string_format_command}")  # Логируем строку  #todo логирование через класс логгеров с разным уровнем

        data = json.loads(string_format_command)
        self.msgCommand=data['msgCommand']
        self.msgID = data['msgID']
        self.msgPayload = data['msgPayload']
    def get(self): #todo форматирование
        map = {
            'msgID': self.msgID, #todo стровоые константы вынести в констаннтый модуль
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
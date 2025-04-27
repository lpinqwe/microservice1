import os
import threading
from src.package_data_to_format.utils.Logger import LoggerAll as log
import pika

import src.package_data_to_format.decor.singletone
from src.package_data_to_format.interfaces.CommandStructure import Command
from src.package_data_to_format.utils.Factory import Factory

from src.package_data_to_format.config.RabbitMQConfig import RabbitMQConfig as RMQC

@src.package_data_to_format.decor.singletone.singleton
class RabbitRabbit:

    def __init__(self, factory: Factory):
        self.factory = factory
        self.properties = pika.BasicProperties(expiration='60000')
        self.credentials = pika.PlainCredentials(username=RMQC.username,
                                                 password=RMQC.password
                                            )

        self.connection_param = pika.ConnectionParameters(host=RMQC.host,
                                                          port=RMQC.port,
                                                          credentials=self.credentials
                                                          )

        self.connection = pika.BlockingConnection(self.connection_param)

        self.channel = self.connection.channel()

        self.publishQue = RMQC.publishQue
        self.watcherQue = RMQC.watcherQue
        self.channel.queue_declare(queue=self.publishQue)
        self.channel.queue_declare(queue=self.watcherQue)

        self.channel.basic_consume(queue=self.watcherQue, on_message_callback=self.callback, auto_ack=False)
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        try:
            tmp = body.decode()

            tmp = Command(tmp)

            tmp = self.factory.execute_command(tmp)

            self.sendMessage(tmp)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception as e:
            ch.basic_nack(delivery_tag=method.delivery_tag)
            tmp = body.decode()

            tmp = Command(tmp)

            log.logger.info(e)
            log.logger.info(tmp)

    def sendMessage(self, msg: Command):
        log.logger.info(msg.msgID)
        self.channel.queue_declare(queue=msg.msgID, durable=False)
        self.channel.basic_publish(
            exchange='',
            routing_key=msg.msgID,  # имя очереди
            body=msg.get(),
            mandatory=True
        )

    def start_consuming(self):
        # можно добавить список для увеличения кол-ва потоков
        # или просто запуск нескольких сервисов
        self.consumerThread = threading.Thread(target=self.receive_messages)
        self.consumerThread.daemon = True
        self.consumerThread.start()

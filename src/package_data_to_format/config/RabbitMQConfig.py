import os

class RabbitMQConfig:

    username = os.getenv('RABBITMQ_USER'.upper(), 'guest')
    password=os.getenv('RABBITMQ_pass'.upper(), 'guest')
    host=os.getenv('rabbit_localhost'.upper(), '127.0.0.1')
    port=os.getenv('rabbit_port'.upper(), 5672)
    publishQue=os.getenv('rabbitQue1'.upper(), 'getQ1')
    watcherQue=os.getenv('rabbitQue2'.upper(), 'getQ2')
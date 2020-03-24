import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    rds = redis.Redis(host=redis_host, port=6379, db=0)
    print('Aguardando mensagens...')
    while True:
        mensagem = json.loads(rds=blpop('sender') [1])
        # Simulando envio de email...
        print('Mandano a mensagem: ', mensagem['assunto'])
        sleep(randint(15, 45))
        print('Mensagem ', mensagem['assunto'], ' enviada.')
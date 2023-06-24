from confluent_kafka import Producer

def send_messages():
    # Configurações do produtor do Kafka
    conf = {'bootstrap.servers': 'localhost:9092'}

    # Cria um produtor Kafka
    producer = Producer(conf)

    # Mensagens a serem enviadas
    messages = ['Mensagem 1', 'Mensagem 2', 'Mensagem 3']

    # Envia as mensagens para o tópico
    for message in messages:
        producer.produce('meu-topico', message.encode('utf-8'))
        producer.flush()

    # Fecha o produtor
    producer.close()

if __name__ == '__main__':
    send_messages()

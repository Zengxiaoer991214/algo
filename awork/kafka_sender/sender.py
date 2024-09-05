from confluent_kafka import Producer

conf = {
    'bootstrap.servers': '10.32.246.160:30463',
    # 'bootstrap.servers': '10.32.246.180:30463',
}

producer = Producer(**conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def send_file_to_kafka(file_path, topic):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    producer.produce(topic, value=file_content, callback=delivery_report)
    producer.poll(0)
    producer.flush()


if __name__ == '__main__':
    file_path = r'E:\开发文档\202409\05 shipment external\msg.txt'
    kafka_topic = 'hes_device_shipment_external'  # Kafka中的目标主题
    send_file_to_kafka(file_path, kafka_topic)

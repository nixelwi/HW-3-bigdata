from kafka import KafkaConsumer

import time
import functools
import random


def simulate_external_request():
    success_probability = 0.7
    if random.random() < success_probability:
        return "Внешний запрос успешен"
    else:
        raise Exception("Внешний запрос завершился неудачей")


def backoff(tries, sleep):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts}/{tries} failed: {e}")
                    if attempts < tries:
                        time.sleep(sleep)
                    else:
                        raise

        return wrapper

    return decorator


@backoff(tries=10, sleep=2)
def message_handler(value) -> None:
    try:
        external_response = simulate_external_request()
        print(f"Поступил внешний запрос. {external_response}")
    except Exception as e:
        print(f"Не удалось обработать внешний запрос. Ошибка: {e}")


def create_consumer():
    print("Connecting to Kafka brokers")
    consumer = KafkaConsumer(
        "zitnerhw3",
        group_id="hw3-group1",
        bootstrap_servers="localhost:29092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
    )

    for message in consumer:
        message_handler(message)
        print(message)


if __name__ == "__main__":
    create_consumer()

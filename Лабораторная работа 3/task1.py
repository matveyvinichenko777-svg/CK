# TODO решите задачу
import json


def task() -> float:
    with open('input.json', encoding='utf-8') as f:
        data = json.load(f)

        total = 0.0
        for item in data:
            total += item["score"] * item["weight"]

        return round(total, 3)

result = task()
print(result)

import random
from typing import Any, Dict, Iterator, List


def filter_by_currency(dict_list: List[Dict[str, Any]]) -> Iterator:
    """Функция для вывода валют транзакции"""
    for operation in dict_list:
        if "operationAmount" in operation:
            currency = operation["operationAmount"]["currency"]["name"]
            yield currency
        elif "operationAmount" or "currency" or "name" not in operation:
            raise KeyError
        else:
            break
